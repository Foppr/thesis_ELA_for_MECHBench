import numpy as np

class MultimodalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for chaotic phase interactions
        self.omega = 2.0 * np.pi
        self.kappa = 2.0
        self.lambda_ = 1.2
        self.mu = 0.5
        # Chaotic scaling factors
        self.chaos_factors = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic oscillatory component with phase modulation
        periodic_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Chaotic frequency modulation based on dimension index and random factors
            freq1 = 1.0 + 0.3 * np.sin(i * 0.7 + self.chaos_factors[i])
            freq2 = 1.5 + 0.4 * np.cos(i * 0.9 + self.chaos_factors[i] * 0.5)
            freq3 = 2.0 + 0.2 * np.sin(i * 1.1 + self.chaos_factors[i] * 0.3)
            
            periodic_sum += (
                0.6 * np.sin(freq1 * xi) +
                0.4 * np.cos(freq2 * xi) +
                0.3 * np.sin(freq3 * xi)
            ) ** 2
            
        # Superquadric radial component with extreme conditioning
        radius = np.linalg.norm(x)
        if radius == 0:
            radial_sum = 0
        else:
            # Superquadric shape with sharp transitions
            radial_sum = (
                self.kappa * radius**2 +
                0.3 * self.lambda_ * radius**4 +
                0.1 * self.mu * radius**6 *
                (1 + 0.5 * np.sin(5 * radius) + 0.4 * np.cos(3 * radius))
            )
            
        # Non-separable cross-dimensional coupling with chaotic interaction
        coupling_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                # Chaotic coupling strength and phase
                coupling_strength = 0.5 + 0.3 * np.sin(i * 0.8 + j * 0.6 + self.chaos_factors[i])
                coupling_phase = self.omega * dist + 0.2 * np.cos(i + j)
                coupling = coupling_strength * np.exp(-dist / (1 + 0.2 * i)) * np.sin(coupling_phase)
                coupling_sum += coupling ** 2
                
        # Asymmetric basin component with extreme penalties
        asymmetric_sum = 0
        for i in range(self.dim):
            xi = x[i]
            # Extreme asymmetric penalties with different exponents
            if xi >= 0:
                asymmetric_sum += 0.8 * xi**4 + 0.2 * xi**5
            else:
                asymmetric_sum += 1.2 * xi**4 + 0.3 * xi**5
                
        # Dimensionality-dependent conditioning and scaling
        scale_factor = 1.0 + 0.5 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.5)
        
        # Combine all components with chaotic weights
        result = scale_factor * (0.7 * periodic_sum + 0.8 * radial_sum + 0.6 * coupling_sum + asymmetric_sum)
        
        # Add chaotic noise for robustness
        noise = 0.005 * np.random.normal(0, 1) * np.prod(self.chaos_factors[:min(3, self.dim)])
        
        return result + noise + 0.3 * self.dim