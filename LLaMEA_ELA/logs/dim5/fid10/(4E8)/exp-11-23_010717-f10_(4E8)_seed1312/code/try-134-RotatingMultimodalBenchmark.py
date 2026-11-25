import numpy as np

class RotatingMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Radial harmonic term with varying frequencies
        radial_harmonic = np.sum(np.sin(2.0 * x) + 0.5 * np.sin(5.0 * x) + 0.3 * np.sin(8.0 * x))
        
        # Angular component with periodic rotation and interference
        angles = np.arctan2(x[1:], x[:-1]) if self.dim > 1 else np.array([0.0])
        angular_terms = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                angular_terms += np.sin(3.0 * angles[i]) * np.cos(4.0 * angles[i]) + \
                                0.7 * np.cos(2.5 * angles[i]) * np.sin(3.5 * angles[i])
        
        # Adaptive conditioning based on dimensionality and position
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (i + 1) * np.abs(x[i])**1.5
            
        # Cross-dimensional interaction with rotating coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(2.0 * x[i]) * np.cos(2.0 * x[j]) + \
                                   np.cos(1.5 * x[i]) * np.sin(1.5 * x[j]) + \
                                   0.5 * np.sin(3.0 * x[i]) * np.sin(3.0 * x[j])
        
        # Periodic grid of local minima with varying amplitudes
        periodic_minima = 0.0
        for i in range(self.dim):
            periodic_minima += 2.0 * np.cos(4.0 * x[i]) + 1.5 * np.sin(6.0 * x[i]) + \
                              0.8 * np.cos(8.0 * x[i]) + 0.3 * np.sin(10.0 * x[i])
        
        # Additional noise with fractal-like characteristics
        noise = 0.2 * np.sum(np.sin(12.0 * x) + np.cos(14.0 * x) + 0.5 * np.sin(17.0 * x))
        
        # Return combined function value
        return radial_harmonic + angular_terms + conditioning + cross_interaction + periodic_minima + noise