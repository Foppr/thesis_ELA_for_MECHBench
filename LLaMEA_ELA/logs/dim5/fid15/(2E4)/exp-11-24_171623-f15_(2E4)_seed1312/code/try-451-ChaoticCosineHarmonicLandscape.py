import numpy as np

class ChaoticCosineHarmonicLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic cosine wave components with varying amplitudes and frequencies
        self.cos_amplitudes = 2.0 + 8.0 * np.random.rand(dim)
        self.cos_frequencies = 15.0 + 25.0 * np.random.rand(dim)
        self.cos_phases = 2.0 * np.pi * np.random.rand(dim)
        # Radial harmonic polynomial components with mixed exponents
        self.harmonic_orders = 3.0 + 6.0 * np.random.rand(dim)
        self.harmonic_coefficients = 0.3 + 4.0 * np.random.rand(dim)
        # Adaptive conditioning with exponential scaling
        self.conditioning_factors = 1.5 + 8.5 * np.random.rand(dim)
        self.conditioning_exponents = 0.5 + 5.0 * np.random.rand(dim)
        # Multi-scale local minima with varying depths and positions
        self.minima_centers = 4.0 * np.random.rand(dim, 30) - 2.0
        self.minima_depths = 0.8 + 5.2 * np.random.rand(30)
        self.minima_radii = 0.1 + 0.8 * np.random.rand(30)
        # Cross-dimensional coupling with asymmetric interaction terms
        self.coupling_strengths = 1.5 + 7.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 0.3 + 3.0 * np.random.rand(dim, dim)
        # Global rotation matrix for complex transformation
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        # Fractal correlation enhancement with multi-scale effects
        self.fractal_factors = 0.5 + 3.0 * np.random.rand(dim)
        self.fractal_exponents = 0.2 + 2.0 * np.random.rand(dim)
        # Dynamic penalty terms with varying weights
        self.penalty_weights = 0.4 + 1.2 * np.random.rand(dim)
        self.penalty_exponents = 1.5 + 4.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic cosine wave component
        cos_sum = 0.0
        for i in range(self.dim):
            cos_sum += self.cos_amplitudes[i] * np.cos(self.cos_frequencies[i] * x_norm[i] + self.cos_phases[i])
        
        # Radial harmonic polynomial component
        harmonic_sum = 0.0
        for i in range(self.dim):
            harmonic_sum += self.harmonic_coefficients[i] * np.power(np.abs(x_norm[i]), self.harmonic_orders[i])
        
        # Adaptive conditioning component
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * np.exp(self.conditioning_exponents[i] * np.abs(x_norm[i]))
        
        # Multi-scale local minima structure
        minima_sum = 0.0
        for k in range(30):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.minima_centers[i, k])**2
            minima_sum += self.minima_depths[k] * np.exp(-dist / (2.0 * self.minima_radii[k]**2))
        
        # Cross-dimensional coupling with asymmetric terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j])
        
        # Combine all components with adjusted weights
        result = 0.25 * cos_sum + 0.22 * harmonic_sum + 0.18 * cond_sum + 0.15 * minima_sum + 0.20 * coupling_sum
        
        # Add rotation and conditioning effects
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.10 * (rotated[0]**6 + rotated[1]**6)
        
        # Dynamic penalty term with varying scaling
        penalty = 0.0
        for i in range(self.dim):
            penalty += self.penalty_weights[i] * np.power(np.abs(x_norm[i]), self.penalty_exponents[i])
        
        # Add fractal correlation enhancement
        fractal_sum = 0.0
        for i in range(self.dim):
            fractal_sum += self.fractal_factors[i] * np.power(np.abs(x_norm[i]), self.fractal_exponents[i])
            
        return result + penalty + 0.15 * fractal_sum