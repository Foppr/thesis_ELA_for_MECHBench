import numpy as np

class FractalEllipticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Self-similar fractal pattern with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            xi = x[i]
            term = xi**6
            for k in range(1, 8):
                term += 0.15 * np.sin(k * xi) * np.cos(k * xi) * (xi**(2 + k % 4))
            fractal += term
            
        # Adaptive elliptic conditioning with position-dependent eccentricity
        elliptic = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.4 * np.sin(0.5 * x[i])**2
            elliptic += eccentricity * (x[i]**2) * np.exp(-0.15 * x[i]**2)
            
        # Dynamic harmonic interference with time-varying phase
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                phase = np.sin(3.0 * dist) + 0.3 * np.cos(2.0 * dist)
                amplitude = 1.0 + 0.5 * np.sin(0.6 * x[i]) * np.cos(0.8 * x[j])
                interference += amplitude * np.sin(phase * dist) * np.exp(-0.08 * dist**2)
                
        # Multi-scale oscillatory landscape with varying frequency and damping
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 1.5 + 0.8 * np.sin(0.4 * x[i])
            damp = 0.1 + 0.2 * np.cos(0.3 * x[i])
            oscillatory += freq * np.sin(freq * x[i]) * np.exp(-damp * np.abs(x[i]))
            
        # Sharp ridge and valley structure with piecewise exponential components
        ridge_valley = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                ridge_valley += 0.4 * np.exp(-0.5 * x[i]**2) + 0.1 * x[i]**4
            else:
                ridge_valley += 0.3 * np.exp(-0.3 * x[i]**2) + 0.2 * x[i]**5
                
        # Cross-term coupling with dynamic weight adjustment
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 + 0.2 * np.sin(0.7 * x[i]) * np.cos(0.9 * x[j])
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                cross_term += weight * np.sin(2.0 * dist) * np.exp(-0.1 * dist**2)
        
        # Combined fitness value with dynamic weighting
        total = 0.3 * fractal + 0.25 * elliptic + 0.2 * interference + 0.15 * oscillatory + 0.08 * ridge_valley + 0.02 * cross_term
        
        return total