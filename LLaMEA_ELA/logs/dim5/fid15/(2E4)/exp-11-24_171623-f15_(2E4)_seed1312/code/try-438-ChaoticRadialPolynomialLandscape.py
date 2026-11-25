import numpy as np

class ChaoticRadialPolynomialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Enhanced chaotic sine wave components with higher frequency variations and quantum-like phases
        self.sine_amplitudes = 4.0 + 8.0 * np.random.rand(dim)
        self.sine_frequencies = 25.0 + 30.0 * np.random.rand(dim)
        self.sine_phases = 2.0 * np.pi * np.random.rand(dim)
        # Modified radial polynomial components with mixed orders and hypercomplex terms
        self.poly_orders = 4.0 + 7.0 * np.random.rand(dim)
        self.poly_coefficients = 0.5 + 3.0 * np.random.rand(dim)
        # Improved adaptive conditioning with logarithmic scaling and exponential factors
        self.conditioning_factors = 2.0 + 7.0 * np.random.rand(dim)
        self.conditioning_exponents = 1.0 + 4.0 * np.random.rand(dim)
        # Refined local minima structure with varying depths, radii, and hyperbolic distortions
        self.minima_centers = 4.0 * np.random.rand(dim, 25) - 2.0
        self.minima_depths = 1.5 + 4.5 * np.random.rand(25)
        self.minima_radii = 0.15 + 1.0 * np.random.rand(25)
        # Enhanced coupling interactions with asymmetric terms and hypercomplex cross-terms
        self.coupling_strengths = 2.0 + 6.0 * np.random.rand(dim, dim)
        self.coupling_exponents = 0.4 + 2.5 * np.random.rand(dim, dim)
        # Quantum-inspired oscillations and hypercomplex cross-terms
        self.quantum_amplitudes = 1.0 + 2.0 * np.random.rand(dim)
        self.quantum_frequencies = 30.0 + 40.0 * np.random.rand(dim)
        # Global rotation matrix with complex transformation
        angle = np.pi * np.random.rand()
        self.rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]])
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic sine wave component with quantum oscillations
        sine_sum = 0.0
        for i in range(self.dim):
            sine_sum += self.sine_amplitudes[i] * np.sin(self.sine_frequencies[i] * x_norm[i] + self.sine_phases[i])
        
        # Modified radial polynomial component with hypercomplex terms
        poly_sum = 0.0
        for i in range(self.dim):
            poly_sum += self.poly_coefficients[i] * np.power(np.abs(x_norm[i]), self.poly_orders[i])
        
        # Improved adaptive conditioning component with exponential factors
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * (np.exp(np.abs(x_norm[i]) ** self.conditioning_exponents[i]) - 1.0)
        
        # Refined local minima structure with hyperbolic distortions
        minima_sum = 0.0
        for k in range(25):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.minima_centers[i, k])**2
            minima_sum += self.minima_depths[k] * np.exp(-dist / (2.0 * self.minima_radii[k]**2))
        
        # Enhanced coupling interactions with asymmetric terms and hypercomplex cross-terms
        coupling_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_sum += self.coupling_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.coupling_exponents[i, j])
        
        # Quantum-inspired oscillations
        quantum_sum = 0.0
        for i in range(self.dim):
            quantum_sum += self.quantum_amplitudes[i] * np.cos(self.quantum_frequencies[i] * x_norm[i])
        
        # Combine all components with adjusted weights
        result = 0.25 * sine_sum + 0.20 * poly_sum + 0.15 * cond_sum + 0.15 * minima_sum + 0.15 * coupling_sum + 0.10 * quantum_sum
        
        # Add rotation and conditioning effects
        if self.dim >= 2:
            rotated = np.dot(self.rotation_matrix, x_norm[:2])
            result += 0.10 * (rotated[0]**6 + rotated[1]**6)
        
        # Mutated penalty term with better scaling and reduced bias - improved version
        penalty = 0.30 * np.sum(np.abs(x_norm)**9) + 0.20 * np.sum(np.sin(12.0 * x_norm)) + 0.15 * np.sum(x_norm**7)
        
        # Add a new global correlation term to increase complexity and discrimination
        correlation_term = 0.08 * np.sum((x_norm[:-1] - x_norm[1:])**3)
        
        return result + penalty + correlation_term