import numpy as np

class TrigonometricRadialCrossLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Trigonometric components with varying frequencies and amplitudes
        self.trig_amplitudes = 2.0 + 4.0 * np.random.rand(dim)
        self.trig_frequencies = 5.0 + 15.0 * np.random.rand(dim)
        # Radial basis functions with dynamic centers and variances
        self.rbf_centers = 5.0 * np.random.rand(dim, 15) - 2.5
        self.rbf_variances = 0.1 + 1.9 * np.random.rand(15)
        # Cross-terms with asymmetric coupling strengths
        self.cross_strengths = 1.0 + 3.0 * np.random.rand(dim, dim)
        self.cross_exponents = 0.5 + 2.5 * np.random.rand(dim, dim)
        # Dynamic conditioning factors
        self.conditioning_factors = 0.5 + 2.5 * np.random.rand(dim)
        # Asymmetric interaction terms
        self.asymmetry_params = 0.1 + 0.9 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Trigonometric oscillation component
        trig_sum = 0.0
        for i in range(self.dim):
            trig_sum += self.trig_amplitudes[i] * np.sin(self.trig_frequencies[i] * x_norm[i])
        
        # Radial basis function component
        rbf_sum = 0.0
        for k in range(15):
            dist = 0.0
            for i in range(self.dim):
                dist += (x_norm[i] - self.rbf_centers[i, k])**2
            rbf_sum += np.exp(-dist / (2.0 * self.rbf_variances[k]))
        
        # Cross-term interactions with asymmetric coupling
        cross_sum = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    asym_factor = 1.0 + self.asymmetry_params[i] * np.sin(x_norm[j])
                    cross_sum += self.cross_strengths[i, j] * np.power(np.abs(x_norm[i] - x_norm[j]), self.cross_exponents[i, j]) * asym_factor
        
        # Dynamic conditioning component
        cond_sum = 0.0
        for i in range(self.dim):
            cond_sum += self.conditioning_factors[i] * (x_norm[i]**2 + np.sin(3.0 * x_norm[i]))
        
        # Combine all components
        result = 0.25 * trig_sum + 0.30 * rbf_sum + 0.20 * cross_sum + 0.25 * cond_sum
        
        # Add penalty term for large values
        penalty = 0.1 * np.sum(np.abs(x_norm)**3)
        
        return result + penalty