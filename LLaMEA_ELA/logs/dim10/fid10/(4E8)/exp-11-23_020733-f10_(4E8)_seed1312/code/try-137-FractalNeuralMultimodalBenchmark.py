import numpy as np

class FractalNeuralMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for each dimension
        self.fractal_dims = np.random.uniform(1.2, 1.8, dim)
        self.neural_weights = np.random.uniform(-1.0, 1.0, (dim, 3))
        self.oscillation_freqs = np.random.uniform(1.0, 5.0, dim)
        self.oscillation_ampls = np.random.uniform(0.5, 2.0, dim)
        self.gating_bias = np.random.uniform(-0.5, 0.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base quadratic term with fractal conditioning
        base_condition = 1.0 + 0.3 * np.sin(np.sum(x**2) / self.dim)
        result += 0.1 * base_condition * np.sum(x**2)
        
        # Fractal sinusoidal components with neural gating
        for i in range(self.dim):
            # Fractional Brownian motion inspired oscillation
            fbm_term = np.sin(self.oscillation_freqs[i] * x[i]) * \
                      np.exp(-0.1 * np.abs(x[i])**self.fractal_dims[i])
            
            # Neural network-like gating mechanism
            gating_input = self.neural_weights[i, 0] * x[i] + \
                          self.neural_weights[i, 1] * np.sin(x[i]) + \
                          self.neural_weights[i, 2] * np.cos(x[i])
            neural_gate = 1.0 / (1.0 + np.exp(-gating_input + self.gating_bias[i]))
            
            # Combined fractal and neural contribution
            term = self.oscillation_ampls[i] * fbm_term * neural_gate
            result += term
            
        # Multi-scale radial basis functions with fractal centers
        for i in range(self.dim):
            # Fractal dynamic center with multiple frequency components
            fractal_center = 2.0 * np.sin(x[i]) + \
                           0.8 * np.cos(2 * x[i]) + \
                           0.4 * np.sin(3 * x[i]) + \
                           0.2 * np.cos(5 * x[i])
            
            # Scale-dependent sigma with fractal modulation
            scale_factor = 0.5 + 0.5 * (1.0 + np.sin(x[i] * 0.5)) * \
                         np.abs(np.cos(x[i] * 0.3))
            sigma = 0.2 * scale_factor
            
            rbf = np.exp(-0.5 * ((x[i] - fractal_center) / sigma)**2)
            result += 1.2 * rbf
            
        # Cross-dimensional coupling with fractal interaction
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Fractal-based coupling strength
                coupling_strength = (1.0 + 
                                   0.4 * np.sin(x[i]) * np.cos(x[j]) +
                                   0.2 * np.sin(2 * x[i] + x[j]) *
                                   np.cos(1.5 * x[i] - x[j]))
                
                # Fractal interaction with multi-scale terms
                interaction = coupling_strength * (np.sin(x[i] + x[j])**3 + 
                                                  np.cos(x[i] - x[j])**3 +
                                                  0.3 * (x[i]**2 - x[j]**2))
                result += 0.5 * interaction
                
        # Adaptive conditioning with fractal modulation
        condition_factor = 1.0 + 0.6 * np.sin(np.sum(x**3) / self.dim + 
                                             0.3 * np.cos(np.sum(x**2)))
        result *= condition_factor
        
        # Add fractal noise with adaptive amplitude
        noise_amplitude = 0.15 * (1.0 + 0.3 * np.abs(np.sin(np.sum(x**3)) + 
                                                    0.2 * np.cos(np.sum(x**4))))
        noise = noise_amplitude * np.sum(np.random.uniform(-1, 1, self.dim))
        result += noise
        
        # Add higher-order fractal polynomial terms
        for i in range(self.dim):
            result += 0.15 * (x[i]**5 - 2*x[i]**3 + x[i])
            
        return result