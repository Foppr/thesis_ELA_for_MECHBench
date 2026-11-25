import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal scaling factors for self-similarity
        self.fractal_factors = [np.sin(i * 0.7) * np.cos(i * 0.3) + 1.5 for i in range(dim)]
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity with scale-dependent modulation
        fractal_term = 0.0
        for i in range(self.dim):
            scale = self.fractal_factors[i % len(self.fractal_factors)]
            freq = 2.0 + 0.5 * np.sin(x[i] * 0.3)
            fractal_term += scale * np.sin(freq * x[i]) * np.cos(0.1 * x[i]**2) * np.exp(-0.05 * x[i]**2)
        
        # Evolutionary path dependency with memory effects
        path_dependency = 0.0
        for i in range(1, self.dim):
            # Memory effect: previous dimension's influence on current
            weight = 0.3 + 0.2 * np.sin(x[i-1] * 0.5)
            path_dependency += weight * (x[i] - x[i-1])**2
        
        # Ruggedness through recursive Gaussian peaks with dynamic centers
        ruggedness = 0.0
        for i in range(self.dim):
            center = x[i] + 0.5 * np.sin(x[i] * 2.0) * np.cos(x[i] * 1.5)
            variance = 0.5 + 0.3 * np.sin(x[i] * 0.7)
            height = 1.0 + 0.4 * np.cos(x[i] * 1.2)
            ruggedness += height * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Scale-invariant potential with multi-harmonic components
        harmonic_potential = 0.0
        for i in range(self.dim):
            harmonic_potential += (np.sin(2.0 * x[i]) + 
                                 0.5 * np.sin(4.0 * x[i]) + 
                                 0.3 * np.sin(6.0 * x[i])) * np.exp(-0.1 * np.abs(x[i]))
        
        # Cross-dimensional coupling with adaptive stiffness
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                stiffness = 1.0 + 0.6 * np.sin(0.5 * (x[i] + x[j]))
                coupling += stiffness * (x[i]**2 - x[j]**2)**2
        
        # Dimensionally varying conditioning
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.0 + 0.5 * np.cos(0.3 * x[i])
            conditioning += cond_factor * x[i]**4
        
        # Combine all components with adaptive weights
        norm_factor = 2.0 + 0.3 * np.log(self.dim + 1)
        
        return (0.25 * fractal_term + 
                0.20 * path_dependency + 
                0.18 * ruggedness + 
                0.15 * harmonic_potential + 
                0.12 * coupling + 
                0.07 * conditioning) * norm_factor