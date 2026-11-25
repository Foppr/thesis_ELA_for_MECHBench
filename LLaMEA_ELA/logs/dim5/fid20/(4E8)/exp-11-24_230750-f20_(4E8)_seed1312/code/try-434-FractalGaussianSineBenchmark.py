import numpy as np

class FractalGaussianSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like parameters with enhanced complexity
        self.fractal_coeffs = np.random.uniform(-3, 3, (dim, 5))
        self.gaussian_centers = np.random.uniform(-4.5, 4.5, dim)
        self.gaussian_widths = np.random.uniform(0.2, 1.8, dim)
        self.sine_weights = np.random.uniform(0.3, 2.5, dim)
        # Add chaotic modulation parameters
        self.chaotic_params = np.random.uniform(0.1, 0.9, dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like Gaussian peaks with multi-scale memory effects
        fractal = 0.0
        for i in range(self.dim):
            center = self.gaussian_centers[i]
            sigma = self.gaussian_widths[i]
            # Multi-scale memory: multiple previous dimensions influence current peak
            mem_factor = 1.0
            for j in range(max(0, i-2), i):
                mem_factor += 0.15 * np.sin(0.7 * x[j] + 0.5 * i)
            fractal += mem_factor * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Enhanced sine-wave couplings with higher-order chaotic modulations
        sine_coupling = 0.0
        for i in range(self.dim):
            weight = self.sine_weights[i]
            # Adaptive weight based on multiple dimensions
            adaptive_weight = weight * (1.0 + 0.4 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[i]))
            for j in range(i+1, min(i+4, self.dim)):
                diff = x[i] - x[j]
                # Enhanced memory coupling with chaotic modulation
                mem_coupling = 1.0 + 0.2 * np.sin(0.4 * (x[i-1] if i > 0 else 0) + 0.3 * x[j])
                # Add chaotic logistic map modulation
                chaotic_mod = 1.0 + 0.15 * (3.9 * (x[i] % 1.0) * (1 - (x[i] % 1.0)))
                sine_coupling += adaptive_weight * mem_coupling * chaotic_mod * np.sin(diff) * np.cos(0.6 * (x[i] + x[j]))
        
        # Enhanced fractal modulation using orthogonal polynomials
        fractal_mod = 0.0
        for i in range(self.dim):
            T = self.fractal_coeffs[i]
            # Use Chebyshev polynomials of the first kind with additional terms
            poly_val = T[0] + T[1]*x[i] + T[2]*np.cos(2*x[i]) + T[3]*np.sin(3*x[i]) + T[4]*np.cos(4*x[i])
            fractal_mod += np.sin(1.8 * x[i]) * poly_val
        
        # Improved adaptive conditioning with dynamic dimension scaling
        cond_factor = 1.0 + 0.3 * np.log(self.dim + 1.0)
        
        # Enhanced cross-dimensional cubic coupling with hyperchaotic modulation
        cubic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Hyperchaotic modulation using multiple logistic maps
                log1 = 3.8 * (x[i] % 1.0) * (1 - (x[i] % 1.0))
                log2 = 3.9 * (x[j] % 1.0) * (1 - (x[j] % 1.0))
                weight = 1.0 + 0.25 * np.sin(log1 + log2)
                cubic_coupling += weight * (x[i]**3 - x[j]**3) * np.cos(0.4 * (x[i] + x[j]))
        
        # Stronger deceptive gradient component with multiple sinusoidal modulations
        deceptive = 0.0
        for i in range(self.dim):
            # Create more complex deceptive valleys using multi-frequency modulation
            deceptive += (np.sin(2.5 * x[i]) * np.cos(0.6 * x[i]) + 
                         0.3 * np.sin(4.0 * x[i]) * np.cos(0.8 * x[i])) * (1.0 + 0.2 * np.sin(2.0 * x[i]))
        
        # Combine all components with updated dynamic weighting
        return (0.20 * fractal + 0.25 * sine_coupling + 0.18 * fractal_mod + 
                0.22 * cubic_coupling + 0.15 * deceptive) * cond_factor