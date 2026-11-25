import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Modified fractal scaling factors for increased complexity
        self.fractal_factors = [np.sin(i * 0.8) * np.cos(i * 0.4) + 1.2 for i in range(dim)]
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like self-similarity with enhanced modulation
        fractal_term = 0.0
        for i in range(self.dim):
            scale = self.fractal_factors[i % len(self.fractal_factors)]
            freq = 2.5 + 0.7 * np.sin(x[i] * 0.4)
            fractal_term += scale * np.sin(freq * x[i]) * np.cos(0.15 * x[i]**2) * np.exp(-0.08 * x[i]**2)
        
        # Enhanced evolutionary path dependency with stronger memory effects
        path_dependency = 0.0
        for i in range(1, self.dim):
            # Stronger memory effect: previous dimension's influence on current
            weight = 0.4 + 0.3 * np.sin(x[i-1] * 0.6)
            path_dependency += weight * (x[i] - x[i-1])**2
        
        # Ruggedness through recursive Gaussian peaks with dynamic centers
        ruggedness = 0.0
        for i in range(self.dim):
            center = x[i] + 0.7 * np.sin(x[i] * 2.5) * np.cos(x[i] * 1.8)
            variance = 0.6 + 0.4 * np.sin(x[i] * 0.8)
            height = 1.2 + 0.5 * np.cos(x[i] * 1.5)
            ruggedness += height * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Scale-invariant potential with multi-harmonic components
        harmonic_potential = 0.0
        for i in range(self.dim):
            harmonic_potential += (np.sin(2.5 * x[i]) + 
                                 0.6 * np.sin(4.5 * x[i]) + 
                                 0.4 * np.sin(6.5 * x[i])) * np.exp(-0.12 * np.abs(x[i]))
        
        # Cross-dimensional coupling with enhanced adaptive stiffness
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                stiffness = 1.2 + 0.8 * np.sin(0.6 * (x[i] + x[j]))
                coupling += stiffness * (x[i]**2 - x[j]**2)**2
        
        # Dimensionally varying conditioning with increased nonlinearity
        conditioning = 0.0
        for i in range(self.dim):
            cond_factor = 1.3 + 0.7 * np.cos(0.4 * x[i])
            conditioning += cond_factor * x[i]**4
        
        # Combine all components with adjusted weights
        norm_factor = 2.5 + 0.4 * np.log(self.dim + 1)
        
        return (0.30 * fractal_term + 
                0.25 * path_dependency + 
                0.20 * ruggedness + 
                0.15 * harmonic_potential + 
                0.08 * coupling + 
                0.02 * conditioning) * norm_factor