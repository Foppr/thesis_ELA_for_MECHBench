import numpy as np

class OscillatoryRadialGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Radial basis function component with sinusoidal modulation
        rbf_term = 0.0
        for i in range(self.dim):
            # Radial distance with sinusoidal perturbation
            r = np.sqrt(np.sum(x**2))
            radial = np.exp(-0.1 * r**2) * (1.0 + 0.3 * np.sin(5.0 * r))
            rbf_term += radial
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.5)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            sin_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Asymmetric gradient field with directional bias
        grad_term = 0.0
        for i in range(self.dim):
            # Directional bias based on position
            bias = 1.0 + 0.5 * np.tanh(x[i] - 1.0)
            grad_term += bias * x[i]**3
        
        # Cross-dimensional coupling with oscillatory interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Oscillatory coupling between dimensions
                coupling = np.sin(2.0 * (x[i] + x[j])) * np.cos(1.5 * (x[i] - x[j]))
                cross_term += coupling
        
        # Multi-modal wells with varying depths and positions
        well_term = 0.0
        for i in range(self.dim):
            # Multiple local minima with different characteristics
            well1 = (x[i] - 2.0)**2 * (x[i] + 2.0)**2
            well2 = (x[i] - 1.0)**4 + 0.5 * (x[i] + 1.0)**4
            well_term += 0.5 * well1 + 0.3 * well2
        
        # Final combination with adaptive weights
        total = 0.3 * rbf_term + 0.25 * sin_term + 0.2 * grad_term + 0.15 * cross_term + 0.1 * well_term
        
        # Global scaling and dimensionality adjustment
        scaling = 1.0 + 0.1 * self.dim + 0.05 * np.sin(self.dim * 0.3)
        
        return total * scaling