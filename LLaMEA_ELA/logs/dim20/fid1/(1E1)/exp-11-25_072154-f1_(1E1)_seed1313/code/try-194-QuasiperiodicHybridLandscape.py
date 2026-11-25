import numpy as np

class QuasiperiodicHybridLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Quasiperiodic trigonometric component with multiple frequencies and phases
        freqs = np.array([1.0, 1.618, 2.718, 3.142, 4.236])
        phases = np.array([0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi])
        trig_component = np.sum(np.sin(freqs * x_scaled[:, None] + phases) * 
                               np.cos(freqs * x_scaled[:, None] + phases), axis=0)
        
        # Polynomial smoothing with adaptive exponents
        poly_component = np.sum((x_scaled**2 + 0.5 * x_scaled**4 + 0.1 * x_scaled**6) * 
                               np.exp(-0.5 * x_scaled**2))
        
        # Gradient-based attraction to multiple local minima with varying strengths
        centers = np.array([[-1, -1], [1, 1], [-1, 1], [1, -1]])
        if self.dim >= 2:
            grad_component = 0.0
            for center in centers:
                dist = np.sqrt(np.sum((x_scaled[:2] - center)**2))
                grad_component += np.exp(-dist**2 / 0.5) / (dist + 0.1)
        else:
            grad_component = 0.0
        
        # Cross-dimensional coupling with dynamic weights based on distance
        if self.dim > 1:
            coupling = 0.0
            for i in range(self.dim - 1):
                coupling += (x_scaled[i]**2 + x_scaled[i+1]**2) * np.sin(5 * (x_scaled[i] - x_scaled[i+1]))
            coupling *= np.exp(-np.sum(x_scaled**2) / 10.0)
        else:
            coupling = 0.0
            
        # Fractal-like self-similarity through recursive scaling
        fractal_component = 0.0
        for i in range(1, min(4, self.dim + 1)):
            if i < self.dim:
                fractal_component += np.sin(2**(i+1) * x_scaled[i-1]) * np.cos(2**i * x_scaled[i])
                
        # Dynamic noise with time-like progression
        noise = np.sum(np.sin(10 * x_scaled + np.arange(self.dim)) * 
                      np.cos(9 * x_scaled + np.arange(self.dim)))
        
        # Combine all components with optimized weights
        return (0.3 * trig_component + 0.25 * poly_component + 0.2 * grad_component + 
                0.15 * coupling + 0.08 * fractal_component + 0.02 * noise)