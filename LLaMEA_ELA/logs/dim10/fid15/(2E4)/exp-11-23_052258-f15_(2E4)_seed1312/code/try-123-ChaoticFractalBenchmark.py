import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute hyperchaotic parameters for increased complexity
        self.fractal_dims = [1.1 + 0.4 * np.sin(i * 0.8) for i in range(dim)]
        self.adaptation_factors = [0.5 + 0.6 * np.cos(i * 0.5) for i in range(dim)]
        self.hyperchaos_params = [2.5 + 1.5 * np.sin(i * 0.3) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperchaotic gradient flow component with multiple logistic maps
        chaotic_term = 0.0
        for i in range(self.dim):
            # Multiple coupled chaotic maps for enhanced complexity
            chaos1 = 4.0 * (x[i] % 1.0) * (1 - x[i] % 1.0)
            chaos2 = 3.8 * np.sin(x[i]) * (1 - np.cos(x[i])**2)
            chaos_term = chaos1 * chaos2
            chaotic_term += chaos_term * np.sin(20 * x[i]) * np.cos(9 * x[i])
            
        # Nested fractal basin boundaries with self-similar attractors
        fractal_term = 0.0
        for i in range(self.dim):
            # Multi-scale fractal structure using fractional dimensions and nested scaling
            fractal_exp = self.fractal_dims[i % len(self.fractal_dims)]
            fractal_term += (np.abs(x[i])**fractal_exp) * np.sin(5 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
            
        # Dynamic conditioning with time-varying factors and strong coupling
        adapt_term = 0.0
        for i in range(self.dim):
            # Time-varying conditioning factor with hyperbolic scaling
            cond_factor = self.adaptation_factors[i % len(self.adaptation_factors)]
            adapt_term += cond_factor * (x[i]**2 + 0.2 * np.sin(15 * x[i])**2) * np.exp(-0.1 * np.abs(x[i]))
            
        # Extended cross-dimensional coupling with hyperbolic interactions (mutated)
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Reduced coupling range
                # Hyperbolic coupling with exponential decay and modified interaction
                coupling = np.tanh(x[i] * x[j]) * (x[i]**3 + x[j]**3) * np.exp(-0.03 * (x[i] - x[j])**2)
                cross_term += coupling
                
        # Ultra-high-frequency oscillatory component with multiple harmonic layers
        osc_term = 0.0
        for i in range(self.dim):
            # Multiple frequency components with varying amplitudes
            freqs = [25.0, 35.0, 45.0, 55.0, 65.0]
            for k, freq in enumerate(freqs):
                osc_term += (k+1) * np.sin(freq * x[i % self.dim]) * np.cos(freq * x[i % self.dim])
                
        # Hyper-asymmetric basins with multiple nested minima and enhanced complexity
        basin_term = 0.0
        for i in range(self.dim):
            # Create hyper-asymmetric parabolic wells with higher non-linearity
            asym = 1.5 + 0.5 * np.sin(0.8 * i)
            basin_term += asym * (x[i] - 0.4 * np.sin(5 * x[i]) + 0.1 * np.cos(3 * x[i]))**2
            
        # Combine all terms with new weights for better balance
        weights = [0.3, 0.25, 0.2, 0.15, 0.1]
        total = (weights[0] * chaotic_term + 
                weights[1] * fractal_term + 
                weights[2] * adapt_term + 
                weights[3] * cross_term + 
                weights[4] * basin_term)
                
        # Add global scaling with enhanced dimensionality and exponential components
        scale = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sum(np.abs(x)) + 0.02 * np.sum(x**4)
        
        return scale * total