import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale to [-5, 5]
        x_scaled = x / 5.0
        
        # Chaotic logistic component with varying parameters
        chaotic_term = 0.0
        r_values = [3.8, 3.9, 4.0, 3.7, 3.6]  # Different chaos parameters
        for i in range(min(self.dim, len(r_values))):
            x_i = x_scaled[i]
            # Logistic map: x_{n+1} = r * x_n * (1 - x_n)
            logistic_val = r_values[i] * x_i * (1 - x_i)
            chaotic_term += 0.5 * np.sin(10 * logistic_val) + 0.3 * np.cos(7 * logistic_val)
            
        # Saddle-point interaction terms with varying strengths
        saddle_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create saddle-like interactions using hyperbolic functions
                saddle_interaction = np.tanh(x[i]) * np.tanh(x[j]) + \
                                    0.3 * np.sinh(0.5 * x[i]) * np.cosh(0.7 * x[j])
                saddle_term += saddle_interaction * (i + j + 1) * 0.1
                
        # Fractal-like curvature using fractional Brownian motion approximations
        fractal_term = 0.0
        for i in range(self.dim):
            # Approximate fractal behavior with multiple frequency components
            fractal_term += (np.sin(x[i] * 2) + 
                            0.5 * np.cos(x[i] * 3) + 
                            0.2 * np.sin(x[i] * 7) +
                            0.1 * np.cos(x[i] * 11) +
                            0.05 * np.sin(x[i] * 17))
            
        # Combined penalty for extreme values (creates irregular basins)
        penalty_term = 0.0
        for i in range(self.dim):
            penalty_term += 2.0 * np.exp(-0.5 * (x[i] / 3.0)**2) + \
                           1.5 * np.abs(x[i])**1.5 + \
                           0.8 * np.sin(0.3 * x[i])**2
            
        # Cross-dimensional coupling with chaotic modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Use a chaotic sequence to modulate coupling strength
                if i + j > 0:
                    coupling_strength = np.sin((i + j) * np.pi / (self.dim + 1)) * 0.5 + 0.5
                    cross_coupling += coupling_strength * x[i] * x[j] * (1 + 0.2 * np.sin(x[i] + x[j]))
                    
        # Global scaling factor with fractal characteristics
        global_scale = 1.0 + 0.3 * np.sin(np.sum(x_scaled**2) * 0.5)
        
        # Combine all terms
        result = global_scale * (chaotic_term + saddle_term + fractal_term + penalty_term + cross_coupling)
        
        # Add a constant offset to ensure the global minimum is not trivially zero
        return result + 3.0