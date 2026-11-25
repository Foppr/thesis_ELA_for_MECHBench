import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Trigonometric chaos component with varying frequencies and amplitudes
        trig_chaos = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * x[i])
            amp = 1.0 + 0.7 * np.cos(0.4 * x[i]**2)
            trig_chaos += amp * np.sin(freq * x[i] + 0.5 * np.cos(1.5 * x[i]))
        
        # Radial basis function with dynamic centers and variances
        radial = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -4.0 + 2.0 * j
                variance = 0.8 + 0.4 * np.sin(0.5 * x[i])
                radial += np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional coupling with radial and trigonometric interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                coupling += (np.sin(dist) + 0.5 * np.cos(2.0 * dist)) * (x[i]**2 + x[j]**2)
        
        # Adaptive conditioning with dimension-dependent scaling
        cond = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[i])
            cond += scale * (x[i]**3 + 0.5 * x[i]**2)
        
        # Shallow local minima with sinusoidal modulation
        shallow = 0.0
        for i in range(self.dim):
            shallow += 0.3 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Dimensionally scaled normalization factor
        norm_factor = 1.5 + 0.2 * np.log(self.dim + 1)
        
        return (0.3 * trig_chaos + 0.25 * radial + 0.2 * coupling + 
                0.15 * cond + 0.1 * shallow) * norm_factor