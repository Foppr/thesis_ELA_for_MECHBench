import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic basin term
        quadratic = np.sum(x**2) / self.dim
        
        # Enhanced periodic multimodal term with multiple global minima and chaotic modulation
        periodic = 0.0
        for i in range(self.dim):
            periodic += (np.sin(30 * np.pi * x[i]) ** 2 + 
                        0.8 * np.cos(20 * np.pi * x[i]) ** 2 + 
                        0.4 * np.sin(25 * np.pi * x[i]) ** 2 +
                        0.2 * np.cos(35 * np.pi * x[i]) ** 2)
        
        # Add interaction terms between dimensions with varying weights and chaotic modulation
        interaction = 0.0
        for i in range(self.dim - 1):
            interaction += (x[i] - x[i+1])**8 + 0.5 * (x[i] + x[i+1])**5 + 0.3 * np.sin(10 * (x[i] - x[i+1]))
        
        # Add cubic interaction terms for increased complexity with dynamic weights
        cubic_interaction = 0.0
        for i in range(self.dim - 2):
            weight = 0.4 + 0.2 * np.sin(5 * x[i])
            cubic_interaction += weight * ((x[i] - x[i+2])**7 + 0.3 * (x[i] + x[i+2])**4)
        
        # Add quartic interaction terms for even higher complexity with varying exponents
        quartic_interaction = 0.0
        for i in range(self.dim - 3):
            exp = 6 + 2 * np.cos(3 * x[i])
            quartic_interaction += (x[i] - x[i+3])**exp + 0.15 * (x[i] + x[i+3])**5
        
        # Add chaotic component using logistic map with dynamic parameter for enhanced complexity
        chaotic = 0.0
        r_values = [3.99, 3.89, 3.79, 3.69, 3.59, 3.49]
        for i in range(self.dim):
            r = r_values[i % len(r_values)] + 0.1 * np.sin(2 * x[i])
            chaotic += np.sin(r * x[i] * (1 - x[i])) ** 2 + 0.25 * np.cos(r * x[i] * (1 - x[i])) ** 2
        
        # Add a dynamic shift based on sine and cosine functions for global minimum with adaptive weights
        shift = 0.0
        for i in range(self.dim):
            weight = 0.7 + 0.3 * np.cos(4 * x[i])
            shift += weight * (0.6 * np.sin(5 * x[i]) + 0.4 * np.cos(7 * x[i]) + 0.2 * np.sin(3 * x[i]))
        
        # Add higher-order polynomial interactions to increase landscape complexity with variable exponents
        high_order = 0.0
        for i in range(self.dim - 4):
            exp = 12 + 3 * np.sin(x[i])
            high_order += (x[i] - x[i+4])**exp + 0.2 * (x[i] + x[i+4])**6
        
        # Add exponential and logarithmic terms to increase complexity and non-linearity with dynamic coefficients
        exp_term = 0.0
        log_term = 0.0
        for i in range(self.dim):
            coeff = 0.8 + 0.2 * np.sin(3 * x[i])
            exp_term += coeff * np.exp(-0.5 * x[i]**2) * np.sin(10 * x[i])
            log_term += coeff * np.log(np.abs(x[i]) + 1) * np.cos(5 * x[i])
        
        # Add a complex correlation term between all dimensions
        corr_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                corr_term += 0.1 * np.sin(np.pi * (x[i] - x[j])) * np.cos(2 * np.pi * (x[i] + x[j]))
        
        # Combine all terms to create challenging landscape
        return quadratic + 0.6 * periodic + 0.3 * interaction + 0.2 * cubic_interaction + 0.1 * quartic_interaction + 0.35 * chaotic + 0.35 * shift + 0.15 * high_order + 0.15 * exp_term + 0.08 * log_term + 0.05 * corr_term