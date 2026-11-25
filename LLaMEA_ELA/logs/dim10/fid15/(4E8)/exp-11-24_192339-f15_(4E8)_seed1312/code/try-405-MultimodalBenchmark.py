import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic polynomial expansion with dynamic coupling
        chaos = 0
        for i in range(self.dim):
            degree = 3 + int(np.abs(x[i]) * 0.7) % 5
            poly_term = np.sum([np.power(x[i], k) * np.sin(0.5 * x[i] * k) for k in range(1, degree + 1)])
            chaos += poly_term * np.exp(-0.15 * x[i]**2)
        
        # Modified radial basis function with fractal scaling
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i in range(self.dim):
            width = 0.3 + 0.4 * (1.0 + np.sin(0.2 * x[i])) / 2.0
            for center in centers:
                rbf += np.exp(-0.3 * ((x[i] - center) / width)**2) * np.cos(0.3 * x[i])
        
        # Dynamic hyperbolic tangent coupling with multi-scale interference
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling += np.tanh(x[i]) * np.tanh(x[j]) * np.exp(-0.15 * (x[i] - x[j])**2) * np.sin(0.2 * (x[i] + x[j]))
        
        # Enhanced oscillatory components with chaotic frequency modulation
        oscillation = 0
        for i in range(self.dim):
            freq = 1.8 + 0.6 * np.sin(0.3 * x[i]) * np.cos(0.4 * x[i])
            scale = 1.0 + 0.5 * np.sin(0.5 * x[i]**2)
            oscillation += scale * np.sin(freq * x[i]) * np.cos(freq * x[i]**3) * np.exp(-0.1 * x[i]**2)
        
        # Fractal basin structure with dynamic transitions
        basin = 0
        for i in range(self.dim):
            transition = 1.0 / (1.0 + np.exp(-3.0 * (x[i] - 2.0)))
            basin += transition * (x[i]**6 - 3*x[i]**4 + 3*x[i]**2 - 1)
        
        # Combine all components with optimized weights for increased complexity
        return 0.25 * chaos + 0.30 * rbf + 0.15 * coupling + 0.25 * oscillation + 0.05 * basin