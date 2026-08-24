import numpy as np

class PolynomialWaveInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with mixed monomials
        poly_component = np.sum(0.3 * (x**4 - 2*x**2 + 1) * np.sin(0.5 * x) + 0.2 * (x**3 - x) * np.cos(0.3 * x))
        
        # Trigonometric wave interference with frequency modulation and phase coupling
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.4 * i)
            phase = 0.2 * np.cos(0.3 * i)
            wave_interference += np.sin(freq * x[i] + phase) * np.cos(freq * x[i] + phase)
        
        # Adaptive scaling based on gradient magnitude and local curvature
        grad_magnitude = np.sum(np.abs(np.gradient(x)))
        scale_factor = 1.0 + 0.3 * np.sin(0.2 * grad_magnitude)
        
        # Multi-scale radial basis with varying bandwidth and center distribution
        radial = 0.0
        for i in range(self.dim):
            center = 2.0 * np.cos(0.5 * i) * np.sin(0.3 * x[i])
            bandwidth = 0.5 + 0.2 * np.sin(0.4 * i)
            radial += np.exp(-0.5 * ((x[i] - center)**2) / bandwidth)
        
        # Coupled harmonic oscillators with time-varying coupling strength
        harmonic = 0.0
        for i in range(self.dim):
            coupling = 0.5 + 0.3 * np.sin(0.2 * i + 0.1 * np.sum(x))
            harmonic += coupling * np.sin(2.0 * x[i] + 0.3 * np.cos(x[i]))
        
        # Cross-term interaction with non-linear coupling
        cross_term = np.sum(0.4 * x * np.sin(0.6 * x) * np.cos(0.4 * x))
        
        # Combine all components with adaptive weighting
        weight_poly = 1.0 + 0.1 * np.sin(0.1 * np.sum(x))
        weight_wave = 1.0 + 0.15 * np.cos(0.2 * np.sum(x))
        weight_radial = 1.0 + 0.2 * np.sin(0.25 * np.sum(x))
        weight_harmonic = 1.0 + 0.1 * np.cos(0.3 * np.sum(x))
        weight_cross = 1.0 + 0.05 * np.sin(0.4 * np.sum(x))
        
        result = (weight_poly * poly_component + 
                 weight_wave * wave_interference + 
                 weight_radial * radial + 
                 weight_harmonic * harmonic + 
                 weight_cross * cross_term) * scale_factor
        
        return result