import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic modulation with fractal scaling
        chaotic_modulation = 0
        for i in range(self.dim):
            # Fractal-like scaling with chaotic component
            scale = 1.0 + 0.5 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            chaotic_modulation += scale * np.exp(-0.1 * x[i]**2) * np.sin(3.0 * np.pi * x[i] + self.dim * 0.7)
        
        # Multi-scale coupling with dynamic interaction
        multi_scale_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Dynamic frequency based on both variables
                freq = 1.5 + 0.8 * np.sin(0.3 * x[i]) * np.cos(0.2 * x[j])
                multi_scale_coupling += np.sin(freq * (x[i] - x[j])) * np.cos(freq * (x[i] + x[j]))
        
        # Dynamic ridge structures with fractal-like variation
        dynamic_ridge = 0
        for i in range(self.dim):
            # Varying degree based on chaotic modulation
            degree = 2 + int(4 * np.sin(0.5 * x[i] + self.dim * 0.4) * np.cos(0.3 * x[i]))
            dynamic_ridge += (x[i]**degree) * np.exp(-0.08 * x[i]**2)
        
        # Multi-scale fractal coupling with chaotic shifts
        fractal_coupling = 0
        for i in range(self.dim):
            shift = 0.3 * np.sin(2.0 * x[i] + self.dim * 0.5)
            for j in range(min(i+2, self.dim)):
                fractal_coupling += np.sin((x[i] + shift) * (x[j] - shift)) * np.cos((x[i] - shift) * (x[j] + shift))
        
        # Combined landscape with weighted components and chaotic scaling
        scale_factor = 1.0 + 0.3 * np.sin(self.dim * 0.2) * np.cos(self.dim * 0.1)
        
        return scale_factor * (0.25 * chaotic_modulation + 0.35 * multi_scale_coupling + 
                              0.25 * dynamic_ridge + 0.15 * fractal_coupling)