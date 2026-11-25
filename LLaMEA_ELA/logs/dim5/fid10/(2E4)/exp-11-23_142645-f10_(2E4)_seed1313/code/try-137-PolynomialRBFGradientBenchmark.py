import numpy as np

class PolynomialRBFGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos components with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x[i]**4 + 0.5 * x[i]**3 - 2.0 * x[i]**2 + 0.8 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Radial basis function coupling with adaptive widths
        rbf_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 1.0 + 0.3 * np.sin(0.5 * (x[i] + x[j]))
                rbf_coupling += np.exp(-0.5 * (dist / width)**2) * (x[i]**2 + x[j]**2) * 1.5
        
        # Adaptive gradient modulation with chaotic scaling
        grad_mod = 0.0
        for i in range(self.dim):
            # Chaotic scaling factor based on position
            scale_factor = 1.0 + 0.4 * np.sin(1.2 * x[i]) * np.cos(0.8 * x[i])
            grad_mod += scale_factor * np.abs(x[i])**1.5
        
        # Multi-scale harmonic interference with dynamic phase shifts
        harmonic = 0.0
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(2.0 * x[i]) + 0.2 * np.cos(1.5 * x[i])
            harmonic += 1.2 * np.sin(4.0 * x[i] + phase_shift) * np.exp(-0.2 * np.abs(x[i]))
        
        # Non-convex valley structure with sharp transitions
        valley_structure = 0.0
        for i in range(self.dim):
            if x[i] < -2.0:
                valley_structure += 2.0 * np.sin(3.0 * x[i]) + 1.5 * x[i]**2
            elif x[i] > 2.0:
                valley_structure += 1.8 * np.cos(2.5 * x[i]) + 2.0 * x[i]**2
            else:
                valley_structure += 0.5 * np.sin(5.0 * x[i]) + 0.3 * x[i]**4
        
        # Combined fitness with dynamic weighting
        total = 0.3 * poly_term + 0.3 * rbf_coupling + 0.2 * grad_mod + 0.15 * harmonic + 0.05 * valley_structure
        
        return total