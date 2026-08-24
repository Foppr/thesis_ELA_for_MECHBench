import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Exponential decay terms with varying rates to induce ruggedness
        exp_decay = np.sum(np.exp(-2.0 * np.abs(x_norm)) * np.sin(3.0 * np.pi * x_norm)**2)
        
        # Trigonometric coupling with multiple frequencies and phase shifts
        trig_coupling = np.sum(np.cos(4.0 * np.pi * x_norm) * np.sin(7.0 * np.pi * x_norm)) + \
                        0.5 * np.sum(np.sin(5.0 * np.pi * x_norm) * np.cos(6.0 * np.pi * x_norm))
        
        # Non-linear polynomial distortions with cross-terms
        poly_distort = np.sum(x_norm**3) + 0.3 * np.sum(x_norm**5) + 0.1 * np.sum(x_norm**7)
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.05 * self.dim
        
        # Add a structured noise term for increased challenge
        noise = 0.05 * np.random.random() * condition_factor
        
        # Combine all components to form the final landscape
        return condition_factor * (exp_decay + trig_coupling + poly_distort) + noise