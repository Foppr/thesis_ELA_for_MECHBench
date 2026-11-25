import numpy as np

class PolynomialTrigBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for polynomial radial components
        self.poly_coeffs = np.random.uniform(0.3, 2.5, dim)
        self.trig_amplitudes = np.random.uniform(1.2, 3.5, dim)
        self.trig_frequencies = np.random.uniform(1.5, 5.0, dim)
        # Conditioning parameters
        self.conditioning_factors = np.random.uniform(0.2, 2.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial radial component
        radius = np.linalg.norm(x)
        if radius == 0:
            radial_term = 0
        else:
            radial_term = sum(self.poly_coeffs[i] * (x[i]**2 + x[i]**4 + 0.3*x[i]**6) for i in range(self.dim))
            
        # Trigonometric cross-terms with adaptive conditioning
        trig_sum = 0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                # Adaptive conditioning based on dimension indices
                cond_i = self.conditioning_factors[i]
                cond_j = self.conditioning_factors[j]
                # Cross-dimensional trigonometric coupling with higher-order terms
                coupling = np.sin(self.trig_frequencies[i] * xi + self.trig_frequencies[j] * xj)
                coupling += 0.5 * np.cos(self.trig_frequencies[i] * xi - self.trig_frequencies[j] * xj)
                coupling += 0.2 * np.sin(2*self.trig_frequencies[i] * xi + 1.5*self.trig_frequencies[j] * xj)
                trig_sum += cond_i * cond_j * coupling**2
                
        # Asymmetric polynomial component
        asym_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Different polynomials for positive and negative values with increased complexity
            if xi >= 0:
                asym_sum += self.trig_amplitudes[i] * (xi**3 + 0.5 * xi**5 + 0.1 * xi**7)
            else:
                asym_sum += self.trig_amplitudes[i] * (1.5 * xi**3 + 0.3 * xi**5 + 0.05 * xi**7)
                
        # Combined fitness with dimensionality scaling
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1)
        
        result = scale_factor * (0.5 * radial_term + 0.6 * trig_sum + 0.4 * asym_sum)
        
        # Add noise for robustness
        noise = 0.01 * np.random.normal(0, 1)
        
        return result + noise + 0.25 * self.dim