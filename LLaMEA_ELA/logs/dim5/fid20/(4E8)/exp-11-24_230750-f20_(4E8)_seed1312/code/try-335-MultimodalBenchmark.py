import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced trigonometric chaos with fractional frequencies and amplitude modulation
        trig_chaos = 0.0
        for i in range(self.dim):
            freq = 3.0 + 2.0 * np.sin(0.4 * x[i]) * np.cos(0.3 * x[i])
            amp = 1.5 + 1.0 * np.sin(0.6 * x[i]**2) * np.cos(0.5 * x[i])
            trig_chaos += amp * np.sin(freq * x[i] + 0.7 * np.cos(1.8 * x[i]) + 0.3 * np.sin(2.2 * x[i]))
        
        # Multi-scale radial basis with dynamic centers, variances, and interaction weights
        radial = 0.0
        for i in range(self.dim):
            for j in range(5):
                center = -4.5 + 2.0 * j
                variance = 1.0 + 0.6 * np.sin(0.7 * x[i] + 0.3 * j)
                weight = 1.0 + 0.5 * np.cos(0.8 * x[i] + 0.4 * j)
                radial += weight * np.exp(-0.5 * ((x[i] - center) / variance)**2)
        
        # Cross-dimensional coupling with multiple interaction types and dynamic scaling
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                coupling += (np.sin(dist) + 0.5 * np.cos(2.0 * dist) + 0.3 * np.sin(3.0 * dist)) * \
                           (x[i]**2 + x[j]**2 + 0.1 * x[i] * x[j])
        
        # Adaptive conditioning with multiple scaling factors and higher-order polynomial terms
        cond = 0.0
        for i in range(self.dim):
            scale1 = 1.0 + 0.8 * np.sin(0.7 * x[i]) * np.cos(0.5 * x[i])
            scale2 = 1.0 + 0.6 * np.sin(0.9 * x[i]**2) * np.cos(0.4 * x[i]**2)
            cond += scale1 * scale2 * (x[i]**4 + 0.7 * x[i]**3 + 0.5 * x[i]**2)
        
        # Shallow local minima with complex sinusoidal modulation and dimensionally varying patterns
        shallow = 0.0
        for i in range(self.dim):
            shallow += 0.4 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * np.sin(0.5 * x[i]**2)
        
        # Additional chaotic component with time-delayed feedback and multi-frequency interactions
        chaotic = 0.0
        for i in range(self.dim):
            if i > 0:
                chaotic += 0.2 * np.sin(x[i] + 0.3 * x[i-1]) * np.cos(1.5 * x[i] + 0.7 * x[i-1])
        
        # Dimensionally scaled normalization factor with exponential growth
        norm_factor = 2.0 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(0.2 * self.dim)
        
        return (0.25 * trig_chaos + 0.3 * radial + 0.25 * coupling + 
                0.15 * cond + 0.05 * shallow + 0.05 * chaotic) * norm_factor