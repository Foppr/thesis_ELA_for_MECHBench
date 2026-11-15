import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with mixed terms
        poly_chaos = np.sum((x**2 + 0.5 * x**3 + 0.1 * x**4) * np.cos(0.5 * x))
        
        # Radial basis function with varying widths and centers
        rbfs = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * np.pi / self.dim)
            width = 0.5 + 0.5 * np.cos(i * np.pi / self.dim)
            rbfs += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Cross-dimensional coupling with trigonometric interactions
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(0.3 * x[i]) * np.cos(0.4 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Hyperbolic tangent modulation with polynomial scaling
        tanh_mod = np.sum(np.tanh(x) * (x**2 + 0.3 * x**3))
        
        # Sine-wave interference pattern with frequency modulation
        sine_pattern = np.sum(np.sin(2.0 * x + 0.5 * np.sin(3.0 * x)) * np.cos(1.5 * x))
        
        # Gaussian mixture with varying amplitudes and positions
        gaussian_mixture = 0.0
        for i in range(5):
            amplitude = 0.2 + 0.1 * i
            position = -4.0 + 2.0 * i
            gaussian_mixture += amplitude * np.exp(-0.5 * ((x - position) / 1.0)**2)
        
        # Fractional polynomial with negative exponents creating singularities
        fractional = np.sum(x**(-1.5) + 0.5 * x**(-2.5) + 0.1 * x**(-3.5))
        
        return poly_chaos + rbfs + cross_coupling + tanh_mod + sine_pattern + gaussian_mixture + fractional