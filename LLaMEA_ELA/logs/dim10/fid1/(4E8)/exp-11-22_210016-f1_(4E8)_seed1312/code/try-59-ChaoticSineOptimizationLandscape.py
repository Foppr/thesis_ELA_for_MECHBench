import numpy as np

class ChaoticSineOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial polynomial component with chaotic sine modulation
        r = np.sqrt(np.sum(x**2))
        radial_poly = 0.0
        for i in range(self.dim):
            radial_poly += (x[i] ** 4) * np.sin(0.5 * r)
        
        # Chaotic sine wave interference with varying amplitudes and frequencies
        sine_wave = 0.0
        for i in range(self.dim):
            sine_wave += np.sin(3.0 * x[i] + 0.7 * r) * np.cos(2.0 * x[i] - 0.3 * r)
        
        # Cross-dimensional quadratic coupling with chaotic phase shifts
        quad_coupling = 0.0
        for i in range(self.dim - 1):
            phase_shift = np.sin(0.5 * (x[i] + x[i+1]))
            quad_coupling += (x[i] * x[i+1]) ** 2 * phase_shift
        
        # Angular-based symmetry breaking with exponential decay
        angular_symmetry = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                angle = np.arctan2(x[i+1], x[i])
                angular_symmetry += np.sin(4.0 * angle) * np.cos(3.0 * angle) * np.exp(-r / 6.0)
        
        # Higher-order trigonometric interaction with radial dependence
        high_order = 0.0
        for i in range(self.dim):
            high_order += np.sin(x[i] ** 3) * np.cos(x[i] ** 2) * np.exp(-r / 3.0)
        
        # Novel chaotic cubic coupling term
        cubic_coupling = 0.0
        for i in range(self.dim - 2):
            cubic_coupling += (x[i] * x[i+1] * x[i+2]) ** 3 * np.sin(0.8 * r)
        
        # Combined with radial exponential decay and sinusoidal modulation
        result = radial_poly + 0.8 * sine_wave + 0.6 * quad_coupling + 0.5 * angular_symmetry + 0.4 * high_order + 0.3 * cubic_coupling
        
        return result