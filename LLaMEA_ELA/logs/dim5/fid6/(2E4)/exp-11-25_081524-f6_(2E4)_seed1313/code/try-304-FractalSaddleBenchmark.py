import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.time = 0.0
        
    def f(self, x):
        self.time += 0.02
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic with time-varying coefficients
        result = np.sum(0.5 * (1.0 + 0.3 * np.sin(self.time)) * x**2)
        
        # Fractal-like multi-modal components with varying scales
        for i in range(self.dim):
            xi = x[i]
            scale = 1.0 + 0.5 * np.sin(0.5 * self.time + i)
            result += scale * (xi**4 - 2*xi**2) * np.exp(-xi**2/4.0)
            
        # Dynamic saddle point configuration with time-varying coupling
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                xi = x[i]
                xj = x[i+1]
                coupling = 0.8 + 0.4 * np.cos(self.time + i)
                result += coupling * (xi**2 - xj**2) * np.sin(2.0 * (xi + xj))
                
        # Harmonic interference with fractal frequency scaling
        for i in range(self.dim):
            xi = x[i]
            freq = 10.0 + 5.0 * np.sin(0.3 * self.time + i)
            result += 0.3 * np.sin(freq * xi) * np.cos(freq * xi / 2.0)
            
        # Time-varying basin depth with multi-scale exponential terms
        for i in range(self.dim):
            xi = x[i]
            depth = 1.5 + 0.8 * np.sin(0.7 * self.time + i)
            result += depth * np.exp(-xi**2/2.0) * (xi**2 + 1.0)**(-1.5)
            
        # Cross-dimensional coupling with fractal-like interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                coupling = 0.6 * np.sin(0.4 * self.time + i + j)
                result += coupling * xi * xj * np.cos(3.0 * (xi - xj))
                
        # Additional fractal-like periodicity with dynamic phase shifts
        for i in range(self.dim):
            xi = x[i]
            phase = 0.5 * self.time + i * 0.2
            result += 0.25 * np.sin(15.0 * xi + phase) * np.cos(8.0 * xi + phase/2.0)
            
        # Multi-scale harmonic interference with varying amplitudes
        for i in range(self.dim):
            xi = x[i]
            amp = 0.7 + 0.3 * np.sin(0.6 * self.time + i)
            result += amp * (np.sin(20.0 * xi) + 0.5 * np.cos(12.0 * xi)) * np.exp(-xi**2/3.0)
            
        # Dynamic curvature with time-varying control parameters
        curv_factor = 1.2 + 0.6 * np.sin(0.8 * self.time)
        result += curv_factor * np.sum(x**3 * np.exp(-x**2/5.0))
        
        return result