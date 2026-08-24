import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Chaotic tent map perturbations with varying control parameters
        tent_map = 0.0
        for i in range(self.dim):
            if x[i] < 0.5:
                tent_map += 2.0 * x[i]
            else:
                tent_map += 2.0 * (1.0 - x[i])
        result += 1.5 * tent_map
        
        # Asymmetric coupled sine-cosine interaction terms
        asym_coupling = 0.0
        for i in range(self.dim - 1):
            asym_coupling += np.sin(x[i] * x[i+1]) * np.cos(x[i] + x[i+1]) * (1.0 + 0.3 * np.sin(x[i] - x[i+1]))
        result += 1.2 * asym_coupling
        
        # Fractional polynomial interactions with non-integer exponents
        frac_poly = 0.0
        for i in range(self.dim):
            frac_poly += 0.8 * (x[i]**2.5 + 0.5 * x[i]**3.7 + 0.2 * x[i]**4.3)
        result += frac_poly
        
        # Novel hyperbolic sine-cosine coupling with exponential decay
        hyperbolic_coupling = 0.0
        for i in range(self.dim - 1):
            hyperbolic_coupling += np.sinh(x[i]) * np.cosh(x[i+1]) * np.exp(-0.1 * (x[i] - x[i+1])**2)
        result += 0.9 * hyperbolic_coupling
        
        # Multimodal Gaussian peaks with varying heights and widths
        gaussian_peaks = 0.0
        for i in range(self.dim):
            gaussian_peaks += 1.8 * np.exp(-0.5 * ((x[i] - 2.0)**2 + (x[i] + 2.0)**2)) * np.cos(3.0 * x[i])**2
        result += gaussian_peaks
        
        # Enhanced chaotic logistic map distortion
        logistic_distortion = 0.0
        r = 3.95
        for i in range(self.dim):
            logistic_distortion += 0.6 * (r * x[i] * (1.0 - x[i]))**2
        result += logistic_distortion
        
        # Saddle point perturbations with modified hyperbolic tangent
        saddle = 0.0
        for i in range(self.dim):
            saddle += 0.4 * np.tanh(x[i]**3) * np.sin(x[i]**2)
        result += saddle
        
        # Novel fractional-order coupling with trigonometric modulation
        frac_coupling = 0.0
        for i in range(self.dim - 1):
            frac_coupling += 0.5 * (x[i]**1.7 + x[i+1]**1.7) * np.cos(2.0 * x[i] * x[i+1])
        result += frac_coupling
        
        return result