import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced trigonometric chaos with fractal-like frequency modulation
        trig_chaos = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i])
            amp = 1.5 + 0.8 * np.sin(0.5 * x[i]**2)
            phase = 0.7 * np.cos(0.6 * x[i])
            trig_chaos += amp * np.sin(freq * x[i] + phase) * np.exp(-0.1 * np.abs(x[i]))
        
        # Dynamic radial basis with elliptical variance and multi-center clustering
        radial = 0.0
        centers = np.linspace(-4.5, 4.5, 5)
        for i in range(self.dim):
            for center in centers:
                variance = 1.2 + 0.6 * np.sin(0.3 * x[i] + center)
                radial += np.exp(-0.5 * ((x[i] - center) / variance)**2) * (1.0 + 0.3 * np.cos(0.4 * x[i]))
        
        # Cross-dimensional coupling with non-linear interaction potentials
        coupling = 0.0
        for i in range(self.dim):
            for j in range(max(0, i-3), min(i+3, self.dim)):
                if i != j:
                    dist = np.sqrt((x[i] - x[j])**2 + 1e-6)
                    coupling += (np.sin(dist) + 0.3 * np.cos(2.0 * dist)) * np.log(1.0 + dist**2)
        
        # Adaptive conditioning with multi-scale scaling factors
        cond = 0.0
        for i in range(self.dim):
            scale1 = 1.0 + 0.4 * np.sin(0.7 * x[i])
            scale2 = 1.0 + 0.3 * np.cos(0.5 * x[i]**2)
            cond += scale1 * scale2 * (x[i]**4 + 0.6 * x[i]**3 + 0.2 * x[i]**2)
        
        # Shallow local minima with multi-frequency sinusoidal modulation
        shallow = 0.0
        for i in range(self.dim):
            shallow += 0.25 * (np.sin(4.0 * x[i]) + 0.5 * np.cos(3.0 * x[i]) + 0.3 * np.sin(6.0 * x[i]))
        
        # Dimensionally adaptive normalization factor
        norm_factor = 2.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(0.5 * self.dim)
        
        return (0.35 * trig_chaos + 0.25 * radial + 0.2 * coupling + 
                0.15 * cond + 0.05 * shallow) * norm_factor