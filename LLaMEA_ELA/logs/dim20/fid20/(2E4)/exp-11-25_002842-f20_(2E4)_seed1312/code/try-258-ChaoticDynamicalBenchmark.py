import numpy as np

class ChaoticDynamicalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Logistic map parameters for each dimension
        self.r_params = np.random.uniform(3.5, 4.0, dim)
        # Time delay for feedback
        self.time_delay = np.random.randint(1, 5, dim)
        # Coupling strengths between dimensions
        self.coupling_strengths = np.random.uniform(0.1, 0.5, (dim, dim))
        # Perturbation parameters
        self.perturbation_magnitudes = np.random.uniform(0.01, 0.1, dim)
        # Delayed feedback coefficients
        self.feedback_coeffs = np.random.uniform(-0.2, 0.2, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Initialize history arrays for delayed feedback
        history = np.zeros((self.dim, max(self.time_delay) + 1))
        for i in range(self.dim):
            history[i, 0] = x[i]
            
        # Iterate through dimensions with chaotic dynamics
        for i in range(self.dim):
            # Initialize chaotic variable
            chaotic_var = x[i]
            # Apply logistic map dynamics with time-delayed feedback
            for t in range(100):  # Burn-in period
                # Current value
                current = chaotic_var
                # Delayed value based on time_delay
                delayed_idx = t % self.time_delay[i]
                delayed_value = history[i, delayed_idx] if t >= self.time_delay[i] else x[i]
                
                # Logistic map with feedback
                chaotic_var = self.r_params[i] * current * (1.0 - current)
                # Add delayed feedback term
                chaotic_var += self.feedback_coeffs[i] * (current - delayed_value)
                # Apply small perturbation
                if t > 50:
                    chaotic_var += np.random.normal(0, self.perturbation_magnitudes[i])
                
                # Update history
                if t < max(self.time_delay) + 1:
                    history[i, t] = current
                    
            # Final chaotic value after burn-in
            final_chaotic = chaotic_var
            
            # Add contribution to fitness
            result += (final_chaotic ** 2) * np.sin(final_chaotic)
            
        # Cross-dimension coupling through perturbed interactions
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term += self.coupling_strengths[i, j] * np.sin(x[i] - x[j])
                    
        # Add coupling to main result
        result += 0.5 * coupling_term
        
        # Add a global scaling factor based on dimensionality
        result *= (1.0 + 0.05 * self.dim)
        
        return result