import numpy as np

class ChaoticGaussianPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillatory components with dynamic amplitudes
        chaotic_osc = 0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(i * 0.6) + 0.3 * np.cos(i * 0.4)
            freq = 1.0 + 0.4 * np.sin(i * 0.8)
            chaotic_osc += amp * np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Gaussian radial basis functions with chaotic centers and variable widths
        rbf_sum = 0
        for i in range(min(10, self.dim)):
            center = -4.0 + 8.0 * (i / max(1, self.dim - 1)) + 0.4 * np.sin(i * 1.2)
            width = 0.2 + 0.6 * np.abs(np.sin(i * 0.6)) + 0.2 * np.cos(i * 0.4)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2) / width**2)
        
        # Polynomial coupling terms with chaotic coefficients and exponents
        poly_coupling = 0
        for i in range(self.dim - 1):
            coeff = 0.6 + 0.4 * np.sin(i * 0.7)
            exp1 = 2 + int(3 * np.sin(i * 0.5))
            exp2 = 3 + int(2 * np.cos(i * 0.6))
            poly_coupling += coeff * (x[i]**exp1 * x[i+1]**exp2) + (1.0 - coeff) * (x[i]**exp2 * x[i+1]**exp1)
        
        # Higher-order polynomial with dynamic exponents and chaotic scaling
        poly_high = 0
        for i in range(self.dim):
            exp_factor = 1.0 + 0.4 * np.sin(i * 0.9)
            poly_high += 0.01 * x[i]**(5 + int(exp_factor * 3)) - 0.03 * x[i]**(4 + int(exp_factor * 2)) + 0.02 * x[i]**(3 + int(exp_factor * 1))
        
        # Dynamic cross-dimensional conditioning with chaotic weights
        conditioning = 0
        for i in range(self.dim - 2):
            weight = 0.7 + 0.3 * np.sin(i * 0.5)
            conditioning += weight * (x[i]**2 + x[i+1]**2 + x[i+2]**2) * np.sin(0.3 * x[i] * x[i+1])
        
        # Deceptive fitness valleys with chaotic modulation
        valley_mod = 0
        for i in range(self.dim):
            valley_mod += 0.1 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all components with dynamic scaling factors
        return 1.5 * chaotic_osc + 1.0 * rbf_sum + 0.6 * poly_coupling + 0.4 * poly_high + 0.3 * conditioning + 0.2 * valley_mod