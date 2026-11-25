import numpy as np

class FractalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like parameters
        self.fractal_coeffs = np.random.uniform(-2, 2, (dim, 4))
        self.gaussian_centers = np.random.uniform(-4, 4, dim)
        self.gaussian_widths = np.random.uniform(0.3, 1.5, dim)
        self.sine_weights = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like Gaussian peaks with memory effects
        fractal = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            # Memory effect: previous dimension values influence current peak
            mem_factor = 1.0
            if i > 0:
                mem_factor = 1.0 + 0.2 * np.sin(0.5 * x[i-1])
            fractal += mem_factor * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Sine-wave couplings with memory and adaptive weights
        sine_coupling = 0.0
        for i in range(self.dim):
            weight = self.sine_weights[i]
            # Adaptive weight based on position
            adaptive_weight = weight * (1.0 + 0.3 * np.sin(0.4 * x[i]))
            for j in range(i+1, min(i+3, self.dim)):
                diff = x[i] - x[j]
                # Memory-enhanced coupling
                mem_coupling = 1.0 + 0.1 * np.cos(0.3 * (x[i-1] if i > 0 else 0))
                sine_coupling += adaptive_weight * mem_coupling * np.sin(diff) * np.cos(0.5 * (x[i] + x[j]))
        
        # Fractal modulation using Chebyshev polynomials
        fractal_mod = 0.0
        for i in range(self.dim):
            T = self.fractal_coeffs[i]
            # Use Chebyshev polynomials of the first kind
            poly_val = T[0] + T[1]*x[i] + T[2]*np.cos(2*x[i]) + T[3]*np.sin(3*x[i])
            fractal_mod += np.sin(1.5 * x[i]) * poly_val
        
        # Adaptive conditioning with dimension-dependent factors
        cond_factor = 1.0 + 0.25 * np.log(self.dim)
        
        # Cross-dimensional cubic coupling with chaotic modulation
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic modulation using logistic map
                logistic_val = 3.8 * (x[i] % 1.0) * (1 - (x[i] % 1.0))
                weight = 1.0 + 0.2 * np.sin(logistic_val)
                cubic_coupling += weight * (x[i]**3 - x[j]**3) * np.cos(0.3 * (x[i] + x[j]))
        
        # Deceptive gradient component
        deceptive = 0.0
        for i in range(self.dim):
            # Create deceptive valleys using sinusoidal modulation
            deceptive += np.sin(2.0 * x[i]) * np.cos(0.5 * x[i]) * (1.0 + 0.1 * np.sin(3.0 * x[i]))
        
        # Combine all components with dynamic weighting
        return (0.25 * fractal + 0.20 * sine_coupling + 0.15 * fractal_mod + 
                0.25 * cubic_coupling + 0.15 * deceptive) * cond_factor