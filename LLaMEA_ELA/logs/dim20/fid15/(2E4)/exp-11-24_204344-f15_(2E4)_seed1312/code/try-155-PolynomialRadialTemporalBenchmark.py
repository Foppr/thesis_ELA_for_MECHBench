import numpy as np

class PolynomialRadialTemporalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos component with fractional exponents
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x[i]**3.5 + 0.5 * x[i]**2.7 + 0.1 * x[i]**1.3) * np.sin(x[i] * 2.0)
        
        # Radial basis function with adaptive centers and widths
        rbf = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(i * 0.7) + 1.0
            width = 0.5 + 0.3 * np.cos(i * 0.5)
            rbf += np.exp(-0.5 * ((x[i] - center) / width)**2) * np.cos(3.0 * x[i])
        
        # Temporal coupling with dynamic phase shifts
        temporal = 0.0
        for i in range(self.dim):
            phase_shift = np.sin(i * 0.3 + np.sum(x[:i]) * 0.1)
            temporal += np.sin(x[i] * 4.0 + phase_shift) * np.cos(x[i] * 2.0 + phase_shift * 0.7)
        
        # Non-smooth chaotic component with piecewise functions
        chaotic = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                chaotic += (x[i]**2.5 + 0.3 * x[i]**1.8) * np.sin(5.0 * x[i])
            else:
                chaotic += (x[i]**3.2 + 0.4 * x[i]**2.1) * np.cos(4.0 * x[i])
        
        # Cross-dimensional interaction with dynamic coupling strengths
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.8 + 0.2 * np.sin(i * j * 0.4 + x[i] * 0.3)
                cross_interaction += coupling_strength * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Multi-scale oscillatory pattern with variable amplitudes
        oscillatory = 0.0
        scales = [1.0, 2.0, 3.0, 4.0]
        for i in range(self.dim):
            for scale in scales:
                oscillatory += np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.5) * (1.0 + 0.2 * np.sin(x[i] * scale * 0.3))
        
        # Asymmetric potential with multiple wells and barriers
        potential = 0.0
        for i in range(self.dim):
            well_depth = 1.5 + 0.5 * np.sin(i * 0.8)
            barrier_height = 0.8 + 0.3 * np.cos(i * 0.6)
            potential += (x[i]**4.0 - 2.0 * x[i]**2.0 + 0.5) * well_depth + barrier_height * np.exp(-0.5 * x[i]**2)
        
        # Fractional power interactions with varying exponents
        fractional = 0.0
        for i in range(self.dim):
            exponent = 1.5 + 0.5 * np.sin(i * 0.4)
            fractional += np.abs(x[i])**exponent * np.cos(x[i] * 3.0)
        
        # Final weighted combination of all components
        return (0.6 * poly_chaos + 0.8 * rbf + 0.7 * temporal + 
                1.2 * chaotic + 0.9 * cross_interaction + 1.1 * oscillatory + 
                1.3 * potential + 1.0 * fractional)