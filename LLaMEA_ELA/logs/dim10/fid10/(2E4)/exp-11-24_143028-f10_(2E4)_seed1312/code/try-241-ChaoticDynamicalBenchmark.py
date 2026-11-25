import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic system parameters
        self.lambdas = np.random.uniform(0.5, 2.0, dim)
        self.delay_times = np.random.uniform(0.1, 1.0, dim)
        self.coupling_strengths = np.random.uniform(0.1, 0.5, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        # Initialize chaotic attractor states
        self.states = np.random.uniform(-1.0, 1.0, dim)
        # Time series parameters
        self.timesteps = 100
        self.dt = 0.01
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize chaotic dynamics
        total_energy = 0.0
        
        for i in range(self.dim):
            # Set initial state for this dimension
            state = self.states[i]
            
            # Simulate chaotic dynamics with time-delayed feedback
            energy = 0.0
            for t in range(self.timesteps):
                # Logistic map with delay and coupling
                delay_idx = (i - int(self.delay_times[i] / self.dt)) % self.dim
                if delay_idx < 0:
                    delay_idx += self.dim
                
                # Chaotic update with coupling from other dimensions
                coupled_state = state + self.coupling_strengths[i] * (
                    np.sin(x[delay_idx] - state + self.phase_shifts[i]) 
                    - np.sin(state)
                )
                
                # Apply logistic map dynamics
                new_state = self.lambdas[i] * coupled_state * (1.0 - coupled_state)
                
                # Energy calculation based on state deviation from equilibrium
                energy += abs(new_state - 0.5) ** 2
                
                state = new_state
            
            total_energy += energy / self.timesteps
        
        # Add phase coupling penalty term
        phase_penalty = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_diff = np.abs(np.sin(x[i] + self.phase_shifts[i]) - 
                                  np.sin(x[j] + self.phase_shifts[j]))
                phase_penalty += phase_diff * self.coupling_strengths[i] * self.coupling_strengths[j]
        
        # Add ergodic mixing component based on x values
        mixing_term = 0.0
        for i in range(self.dim):
            # Create mixing effect using trigonometric functions
            mixing_term += np.sin(x[i]) * np.cos(x[i] * 2) * np.exp(-0.1 * abs(x[i]))
        
        # Combine all components with adaptive weights based on dimensionality
        adaptive_weight = np.log(self.dim + 1) + 1.0
        result = adaptive_weight * total_energy + 0.5 * phase_penalty + 0.3 * mixing_term
        
        return result