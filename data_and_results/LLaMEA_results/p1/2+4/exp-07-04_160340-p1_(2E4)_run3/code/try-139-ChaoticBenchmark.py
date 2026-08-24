import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
        # Initialize chaotic system parameters
        self.r = 3.95
        self.tau = 1
        self.alpha = 0.1
        self.beta = 0.05
        
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x_norm = x / 5.0
        
        # Initialize chaotic map values
        chaotic_values = np.zeros(self.dim)
        x_prev = np.zeros(self.dim)
        
        # Simulate a system of coupled delayed logistic maps
        for t in range(100):  # Burn-in period
            x_new = np.zeros(self.dim)
            for i in range(self.dim):
                # Delayed feedback term
                if t >= self.tau:
                    delayed_x = x_prev[i - self.tau] if i >= self.tau else x_prev[-1]
                else:
                    delayed_x = x_prev[i]
                
                # Coupling term with neighbors
                coupling = 0.0
                for j in range(self.dim):
                    if i != j:
                        coupling += 0.05 * (x_prev[j] - x_prev[i])
                
                # Logistic map with delayed feedback and coupling
                x_new[i] = self.r * x_prev[i] * (1 - x_prev[i]) + \
                           self.alpha * delayed_x + \
                           self.beta * coupling
                
                # Apply bounds to prevent overflow
                x_new[i] = np.clip(x_new[i], -2, 2)
            
            x_prev = x_new
        
        # Compute final chaotic state
        final_state = np.zeros(self.dim)
        for i in range(self.dim):
            if i >= self.tau:
                delayed_x = x_prev[i - self.tau]
            else:
                delayed_x = x_prev[-1]
            
            coupling = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling += 0.05 * (x_prev[j] - x_prev[i])
            
            final_state[i] = self.r * x_prev[i] * (1 - x_prev[i]) + \
                             self.alpha * delayed_x + \
                             self.beta * coupling
        
        # Calculate objective function based on chaotic dynamics
        # Add a quadratic penalty for deviation from zero
        penalty = np.sum(final_state**2)
        
        # Add a periodic modulation term based on input coordinates
        modulation = 0.0
        for i in range(self.dim):
            modulation += 0.3 * np.sin(10 * x[i]) * np.cos(5 * x[i]) + \
                          0.2 * np.sin(15 * x[i]) * np.cos(8 * x[i]) + \
                          0.1 * np.sin(20 * x[i])
        
        # Add a multi-scale fractal-like interaction term
        fractal_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                fractal_interaction += 0.02 * np.sin(25 * dist) * np.cos(12 * dist) * \
                                      np.exp(-0.1 * dist**2)
        
        # Combine all terms
        result = penalty + modulation + fractal_interaction
        
        # Add a global scaling factor to control difficulty
        result *= (1.0 + 0.2 * np.sum(np.abs(x_norm)))
        
        return result