import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-wave modulations with varying frequencies and amplitudes
        trig_chaos = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * x[i] + 1.0)
            amp = 1.5 + 1.2 * np.cos(0.6 * x[i]**2 + 0.5)
            trig_chaos += amp * np.sin(freq * x[i] + 0.7 * np.cos(2.0 * x[i]) + 0.3 * np.sin(1.2 * x[i]))
        
        # Dynamic Gaussian peak structures with time-varying centers and variances
        radial = 0.0
        for i in range(self.dim):
            for j in range(4):
                center = -4.5 + 3.0 * j
                variance = 1.0 + 0.8 * np.sin(0.7 * x[i] + 0.2 * j)
                radial += np.exp(-0.5 * ((x[i] - center) / variance)**2) * (1.0 + 0.3 * np.cos(0.5 * x[i]))
        
        # Cross-dimensional polynomial couplings with adaptive interaction strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                strength = 1.0 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                coupling += strength * (np.sin(dist) + 0.6 * np.cos(2.5 * dist)) * (x[i]**2 + x[j]**2 + 0.1 * x[i] * x[j])
        
        # Adaptive conditioning with dimensionally varying scaling factors
        cond = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.8 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i]) * np.tan(0.3 * x[i])
            cond += scale * (x[i]**4 + 0.6 * x[i]**3 + 0.3 * x[i]**2)
        
        # Shallow local minima with asymmetric sinusoidal modulation
        shallow = 0.0
        for i in range(self.dim):
            shallow += 0.4 * np.sin(4.0 * x[i]) * np.cos(1.5 * x[i]) + 0.2 * np.sin(2.0 * x[i])**2
        
        # Dimensionally scaled normalization factor with logarithmic growth
        norm_factor = 2.0 + 0.3 * np.log(self.dim + 2)
        
        return (0.4 * trig_chaos + 0.3 * radial + 0.25 * coupling + 
                0.15 * cond + 0.1 * shallow) * norm_factor