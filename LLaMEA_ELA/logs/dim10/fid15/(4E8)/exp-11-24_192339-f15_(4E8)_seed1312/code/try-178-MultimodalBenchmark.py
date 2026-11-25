import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_component = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.2 * x[i])
            amp = 1.0 + 0.3 * np.cos(0.3 * x[i])
            sin_component += amp * np.sin(freq * x[i] + np.cos(x[i]))
        
        # Radial symmetry with Gaussian kernels
        radial_component = 0
        for i in range(self.dim):
            dist = np.sqrt(np.sum((x - x[i])**2))
            width = 1.0 + 0.2 * np.sin(0.4 * x[i])
            radial_component += np.exp(-0.5 * (dist / width)**2) * np.cos(dist)
        
        # Cross-dimensional quadratic interactions with coupling strengths
        quad_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 1.0 + 0.4 * np.sin(0.5 * (x[i] + x[j]))
                quad_component += coupling * (x[i]**2 + x[j]**2) * np.tanh(x[i] - x[j])
        
        # Asymmetric skewing and dynamic conditioning
        skew_component = 0
        for i in range(self.dim):
            skew = 1.0 + 0.2 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[i])
            cond = 1.0 + 0.1 * np.sin(0.5 * x[i]**2)
            skew_component += skew * cond * np.tanh(x[i]) * (x[i]**3 + 0.5 * x[i]**2)
        
        # Fractal-like recursive structure with anti-symmetric coupling terms
        fractal_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                fractal_component += (term + np.sin(term)) * np.tanh(x[i] - x[j])
        
        # Global scaling factor
        scale = 1.0 + 0.2 * np.sin(self.dim * 0.1)
        
        # Combine all components with optimized weights
        return scale * (0.3 * sin_component + 0.25 * radial_component + 
                       0.2 * quad_component + 0.15 * skew_component + 
                       0.1 * fractal_component)