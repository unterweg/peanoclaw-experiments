#!/usr/bin/env python
# encoding: utf-8

"""
2D shallow water equations.
"""
#===========================================================================
# Import libraries
#===========================================================================

import numpy as np
#from clawpack.petclaw import plot

def qinit(state):
    # Riemann states of the dam break problem
    damRadius = 0.25
    hl = 1. #2.
    ul = 0.
    vl = 0.
    hr = 1.
    ur = 0.
    vr = 0.
    x0=0.5
    y0=0.5
    xCenter = state.grid.x.centers
    yCenter = state.grid.y.centers
    Y,X = np.meshgrid(yCenter,xCenter)
    r = np.sqrt((X-x0)**2 + (Y-y0)**2)
    state.q[0,:,:] = hl*(r<=damRadius) + hr*(r>damRadius)
    state.q[1,:,:] = hl*ul*(r<=damRadius) + hr*ur*(r>damRadius)
    state.q[2,:,:] = hl*vl*(r<=damRadius) + hr*vr*(r>damRadius)
    
def init(x, y, h):
    return f(x,y)

    
def shallow2D(outdir='./_output'):
    #===========================================================================
    # Import libraries
    #===========================================================================
    import numpy as np
    import peanoclaw
    from clawpack import pyclaw

    #===========================================================================
    # Setup solver and solver parameters
    #===========================================================================
    subdivisionFactor = patchSize
    from clawpack import riemann
    solver = pyclaw.ClawSolver2D(riemann.shallow_roe_with_efix_2D)
    solver.dimensional_split=1
    solver.limiters = pyclaw.limiters.tvd.MC
    
    #Peano solver
    global useHeapCompression
    global fixedTimestepSize
    global forkLevelIncrement
    global reduceReductions
    internal_settings = peanoclaw.InternalSettings(use_heap_compression=useHeapCompression, enable_peano_logging=True, fixed_timestep_size=fixedTimestepSize, fork_level_increment=forkLevelIncrement,reduce_reductions=reduceReductions)
    peanoSolver = peanoclaw.Solver(solver, (1./(gridSize)), qinit,internal_settings=internal_settings)

    #solver.rp = riemann.rp2_shallow_roe_with_efix
    solver.num_waves = 3

    solver.bc_lower[0] = pyclaw.BC.wall
    solver.bc_upper[0] = pyclaw.BC.wall
    solver.bc_lower[1] = pyclaw.BC.wall
    solver.bc_upper[1] = pyclaw.BC.wall
    
    solver.dt_initial = 0.1

    #===========================================================================
    # Initialize domain and state, then initialize the solution associated to the 
    # state and finally initialize aux array
    #===========================================================================

    # Domain:
    xlower = 0.0
    xupper = 1.0
    ylower = 0.0
    yupper = 1.0
    if(usePeano):
        mx = subdivisionFactor
        my = subdivisionFactor
    else:
        mx = gridSize
        my = gridSize
    x = pyclaw.Dimension('x',xlower,xupper,mx)
    y = pyclaw.Dimension('y',ylower,yupper,my)
    domain = pyclaw.Domain([x,y])

    num_eqn = 3  # Number of equations
    state = pyclaw.State(domain,num_eqn)

    grav = 1.0 # Parameter (global auxiliary variable)
    state.problem_data['grav'] = grav

		# ================
    # Initial solution
    # ================
    qinit(state) # This function is defined above

    #===========================================================================
    # Set up controller and controller parameters
    #===========================================================================
    claw = pyclaw.Controller()
    claw.keep_copy = False
    claw.tfinal = tfinal
    if(usePeano): 
      claw.solver = peanoSolver
      claw.solution = peanoclaw.Solution(state,domain)
    else:
      claw.solver = solver
      claw.solution = pyclaw.Solution(state,domain)
    claw.outdir = outdir
    claw.num_output_times = 1

    #===========================================================================
    # Solve the problem
    #===========================================================================
    #status = claw.run()
    return claw

if __name__=="__main__":
    from clawpack.pyclaw.util import run_app_from_main
    import sys
   
#    global gridSize
#    gridSize = int(sys.argv[len(sys.argv)-6])
#    
#    global patchSize
#    patchSize = int(sys.argv[len(sys.argv)-5])
#    
#    global tfinal
#    tfinal = 1.0/float(sys.argv[len(sys.argv)-4])
#    
#    global usePeano
#    usePeano = bool(int(sys.argv[len(sys.argv)-3]))
#    
#    global useHeapCompression
#    useHeapCompression = bool(int(sys.argv[len(sys.argv)-2]))
    
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument("gridSize", type=int)
    parser.add_argument("patchSize", type=int)
    parser.add_argument("tfinal", type=float)
    parser.add_argument("usePeano", type=int)
    parser.add_argument("useHeapCompression", type=int)
    parser.add_argument("fixedTimestepSize", nargs="?", type=float, default=None)
    parser.add_argument("forkLevelIncrement", type=int)
    parser.add_argument("reduceReductions", type=int)
    arguments = parser.parse_args()
    
    global gridSize
    gridSize = arguments.gridSize
    global patchSize
    patchSize = arguments.patchSize
    global tfinal
    tfinal = 1.0/float(arguments.tfinal)
    global usePeano
    usePeano = arguments.usePeano
    global useHeapCompression
    useHeapCompression = arguments.useHeapCompression
    global fixedTimestepSize
    fixedTimestepSize = arguments.fixedTimestepSize
    global forkLevelIncrement
    forkLevelIncrement = arguments.forkLevelIncrement
    global reduceReductions
    reduceReductions = arguments.reduceReductions
    
    output = run_app_from_main(shallow2D)
    #if(not output == None):
    #    print 'Error: ', output





