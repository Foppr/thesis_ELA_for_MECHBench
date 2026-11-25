import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.attractor_strength = 2.0
        self.gradient_noise = 0.8
        self.correlation_decay = 0.15
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient field with exponential decay correlations
        gradient_field = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Exponentially decaying correlation with other dimensions
            corr_factor = np.exp(-self.correlation_decay * sum(abs(x[j] - xi) for j in range(self.dim) if j != i))
            
            # Chaotic gradient term with sinusoidal modulation and dynamic scaling
            grad_term = (xi**3 - 2*xi**2 + xi) * corr_factor * np.sin(xi * 3.14159) * np.exp(-0.1 * xi**2)
            gradient_field += grad_term
        
        # Dynamic basin boundaries with multiple local minima
        basin_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Create multiple basins with varying depths and chaotic positioning
            basin_depth = 1.0 + 0.5 * np.sin(xi * 2.0) + 0.3 * np.cos(xi * 1.5)
            basin_width = 0.8 + 0.2 * np.sin(xi * 1.7)
            
            # Basin potential with chaotic modulation
            basin_potential = basin_depth * (xi**4 - 2*xi**2) * np.exp(-0.1 * xi**2)
            basin_term += basin_potential
            
        # Exponentially decaying correlation landscape with chaotic amplitude modulation
        correlation_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Correlation with all other dimensions using exponential decay
            corr_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    corr_sum += np.exp(-self.correlation_decay * abs(xi - x[j])) * np.sin(xi + x[j])
            
            correlation_term += corr_sum * np.cos(xi * 2.5) * np.exp(-0.05 * xi**2)
        
        # Chaotic noise term with dynamic frequency and amplitude
        noise_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add chaotic noise with varying frequency based on dimension position
            freq = 1.0 + 0.5 * np.sin(i * 0.7)
            amp = 0.3 + 0.2 * np.cos(i * 0.9)
            noise_term += amp * np.sin(xi * freq) * np.exp(-0.1 * xi**2)
        
        # Asymmetric radial component with chaotic curvature
        radial_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Radial term with asymmetric behavior and chaotic modulation
            if xi >= 0:
                radial_term += (xi**5 - 3*xi**3 + xi) * np.exp(-0.2 * xi**2)
            else:
                radial_term += (xi**4 - 2*xi**2) * np.exp(-0.15 * xi**2)
        
        # Combine all terms with proper scaling
        return 0.8 * gradient_field + 1.2 * basin_term + 0.9 * correlation_term + 0.6 * noise_term + 0.7 * radial_term