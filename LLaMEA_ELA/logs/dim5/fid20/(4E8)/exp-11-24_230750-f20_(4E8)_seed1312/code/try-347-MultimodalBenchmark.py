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
            freq = 2.5 + 3.0 * np.sin(0.5 * x[i] + 1.2)
            amp = 2.0 + 1.5 * np.cos(0.7 * x[i]**2 + 0.6)
            trig_chaos += amp * np.sin(freq * x[i] + 0.8 * np.cos(2.5 * x[i]) + 0.4 * np.sin(1.5 * x[i]))
        
        # Dynamic Gaussian peak structures with time-varying centers and variances
        radial = 0.0
        for i in range(self.dim):
            for j in range(3):
                center = -4.0 + 2.5 * j
                variance = 1.2 + 0.9 * np.sin(0.8 * x[i] + 0.3 * j)
                radial += np.exp(-0.5 * ((x[i] - center) / variance)**2) * (1.2 + 0.4 * np.cos(0.6 * x[i]))
        
        # Cross-dimensional polynomial couplings with adaptive interaction strengths
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                strength = 1.5 + 0.7 * np.sin(0.4 * (x[i] + x[j]))
                coupling += strength * (np.sin(dist) + 0.7 * np.cos(3.0 * dist)) * (x[i]**2 + x[j]**2 + 0.15 * x[i] * x[j])
        
        # Adaptive conditioning with dimensionally varying scaling factors
        cond = 0.0
        for i in range(self.dim):
            scale = 1.5 + 1.0 * np.sin(0.8 * x[i]) * np.cos(0.6 * x[i]) * np.tan(0.4 * x[i])
            cond += scale * (x[i]**4 + 0.7 * x[i]**3 + 0.4 * x[i]**2)
        
        # Shallow local minima with asymmetric sinusoidal modulation
        shallow = 0.0
        for i in range(self.dim):
            shallow += 0.5 * np.sin(5.0 * x[i]) * np.cos(2.0 * x[i]) + 0.3 * np.sin(2.5 * x[i])**2
        
        # Enhanced deceptive gradient components with saddle-point interactions
        decept = 0.0
        for i in range(self.dim):
            decept += 0.2 * np.sin(3.0 * x[i]) * np.cos(1.8 * x[i]) + 0.15 * np.sin(4.5 * x[i])**3
        
        # Dimensionally scaled normalization factor with logarithmic growth
        norm_factor = 2.5 + 0.4 * np.log(self.dim + 3)
        
        return (0.35 * trig_chaos + 0.28 * radial + 0.22 * coupling + 
                0.18 * cond + 0.12 * shallow + 0.07 * decept) * norm_factor