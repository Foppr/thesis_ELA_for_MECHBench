import numpy as np

class ChaoticDelayedLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r_values = 3.9 + 0.1 * np.random.rand(dim)
        self.delay = 2 + np.random.randint(0, 3, dim)
        self.feedback_strength = 0.3 + 0.4 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [0, 1] range
        x_norm = (x + 5.0) / 10.0
        
        # Initialize chaotic system
        state = x_norm.copy()
        total_energy = 0.0
        
        # Iterate through multiple time steps for each dimension
        for t in range(20):
            new_state = np.zeros_like(state)
            
            for i in range(self.dim):
                # Time-delayed logistic map with parameter perturbation
                delayed_idx = (i - self.delay[i]) % self.dim
                r_perturbed = self.r_values[i] * (1.0 + 0.05 * np.sin(t * 0.1))
                
                # Chaotic dynamics with delayed feedback
                if t >= self.delay[i]:
                    feedback = state[delayed_idx]
                else:
                    feedback = x_norm[delayed_idx]
                    
                new_state[i] = r_perturbed * state[i] * (1.0 - state[i]) + \
                              self.feedback_strength[i] * (feedback - state[i])
                
                # Add coupling between dimensions
                if i > 0:
                    new_state[i] += 0.02 * np.sin(state[i-1] - state[i])
                    
            state = new_state
            
        # Energy-based fitness calculation with multiple attractor interactions
        for i in range(self.dim):
            # Multiple coexisting attractors with different basins
            attractor1 = np.sin(2 * np.pi * state[i]) ** 2
            attractor2 = np.cos(3 * np.pi * state[i]) ** 2
            attractor3 = np.tanh(5 * (state[i] - 0.5)) ** 2
            
            # Weighted combination with dynamic weights
            weight1 = 0.3 + 0.4 * np.sin(t * 0.2 + i)
            weight2 = 0.3 + 0.4 * np.cos(t * 0.3 + i)
            weight3 = 0.4 + 0.3 * np.sin(t * 0.1 + i)
            
            total_energy += weight1 * attractor1 + weight2 * attractor2 + weight3 * attractor3
            
        # Add noise term for stochastic behavior
        noise = 0.05 * np.sum(np.random.randn(self.dim) * state)
        
        # Add polynomial regularization to control conditioning
        poly_term = 0.1 * np.sum(state ** 3 + 0.5 * state ** 4)
        
        return total_energy + noise + poly_term