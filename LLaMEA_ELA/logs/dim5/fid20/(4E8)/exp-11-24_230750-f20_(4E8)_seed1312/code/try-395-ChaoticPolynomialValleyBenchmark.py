import numpy as np

class ChaoticPolynomialValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic parameter initialization with memory effects
        self.coupling_coeffs = 2.0 * np.random.rand(dim) - 1.0
        self.oscillation_freqs = 1.0 + 3.0 * np.random.rand(dim)
        self.polynomial_degrees = 3 + np.random.randint(2, 6, dim)
        # Memory-dependent valley centers
        self.valley_centers = np.random.uniform(-4, 4, (dim, 2))
        # Time-varying conditioning factors
        self.time_mod = 1.0 + 0.3 * np.sin(0.1 * dim)
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic polynomial valley components with memory
        valley = 0.0
        for i in range(self.dim):
            # Base polynomial with dynamic degree and coupling
            poly_term = (x[i] ** self.polynomial_degrees[i]) * self.coupling_coeffs[i]
            # Memory effect from previous dimension
            mem_effect = 0.1 * np.sin(0.5 * x[max(0, i-1)])
            valley += poly_term * (1.0 + mem_effect)
        
        # Dynamic harmonic oscillations with time dependency
        oscillation = 0.0
        for i in range(self.dim):
            freq = self.oscillation_freqs[i] * self.time_mod
            osc_component = np.sin(freq * x[i]) * np.cos(0.5 * x[i])
            # Adaptive amplitude based on position and dimension
            amp = 1.5 + 0.5 * np.sin(0.3 * x[i]) + 0.2 * np.cos(0.4 * i)
            oscillation += amp * osc_component
        
        # Cross-dimensional polynomial coupling with memory
        coupling = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Memory-enhanced coupling between dimensions
                mem_coupling = 0.3 * np.sin(0.4 * x[i]) * np.cos(0.2 * x[max(0, i-1)])
                coupling += (x[i] ** 2) * (x[i+1] ** 2) * mem_coupling
        
        # Memory-dependent conditioning with exponential modulation
        cond = 0.0
        for i in range(self.dim):
            # Conditioned by previous dimension and time
            cond_factor = 1.0 + 0.2 * np.sin(0.6 * x[i]) + 0.1 * np.cos(0.3 * x[max(0, i-1)]) + 0.05 * np.sin(0.1 * self.time_mod)
            # Exponential weighting based on position
            weight = np.exp(-0.5 * x[i]**2) * cond_factor
            cond += weight * (x[i] ** 3)
        
        # Valley center attraction with time modulation
        attraction = 0.0
        for i in range(self.dim):
            center1, center2 = self.valley_centers[i]
            # Time-varying attraction strength
            attr_strength = 1.0 + 0.2 * np.sin(0.2 * self.time_mod)
            attraction += (x[i] - center1)**2 + (x[i] - center2)**2 * attr_strength
        
        # Combine all components with dimension scaling
        dim_scale = 1.0 + 0.1 * np.log(self.dim) + 0.05 * np.cos(0.3 * self.dim)
        return (0.35 * valley + 0.25 * oscillation + 0.20 * coupling + 
                0.15 * cond + 0.05 * attraction) * dim_scale