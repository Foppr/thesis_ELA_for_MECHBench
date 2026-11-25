import numpy as np

class FractalAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 2.7  # Increased fractional dimension for more complex structure
        self.attraction_strength = 2.0
        self.frequency_base = 4.0
        self.quantum_factor = 0.8
        self.adaptive_coupling = 0.25
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create quantum-inspired fractal pattern with interference effects
        fractal_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            scale = 2 ** (i % 5)
            freq = self.frequency_base * scale
            # Quantum interference terms
            quantum_term = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.3) * \
                          np.sin(freq * x_norm[i] * 0.7) * np.cos(freq * x_norm[i] * 1.2)
            fractal_pattern[i] = quantum_term + 0.3 * np.sin(freq * x_norm[i] * 2.0)
        
        # Enhanced attraction fields with dynamic basins
        attraction_fields = np.zeros(self.dim)
        for i in range(self.dim):
            center_points = np.array([-0.9, -0.5, -0.1, 0.3, 0.6, 0.9])
            strengths = np.array([1.5, 1.2, 0.8, 1.0, 0.7, 1.3])
            
            distances = np.abs(x_norm[i] - center_points)
            attraction_fields[i] = np.sum(strengths * np.exp(-distances**2.5))
        
        # Combine fractal pattern with enhanced attraction fields
        combined_pattern = fractal_pattern + 0.6 * attraction_fields
        
        # Add quantum-inspired curvature terms with higher-order polynomials
        curvature_term = np.sum(combined_pattern**5) + 0.4 * np.sum(combined_pattern**7)
        
        # Introduce dynamic coupling with time-like progression
        coupling_term = self.adaptive_coupling * np.sum((x_norm[1:] - x_norm[:-1])**4)
        
        # Add quantum tunneling effects and non-smooth features
        quantum_tunneling = 0.3 * np.sum(np.abs(x_norm)**1.3)
        
        # Introduce adaptive penalty based on dimensionality and solution distribution
        penalty = 0.1 * self.dim * (np.std(x_norm)**2 + 0.05 * np.mean(np.abs(x_norm)))
        
        # Add basin complexity factor that scales with dimensionality
        basin_complexity = 0.08 * self.dim * np.sum(np.sin(3.0 * x_norm)**2)
        
        # Final fitness calculation with enhanced adaptive scaling
        adaptive_scale = 1.0 + 0.02 * np.log(self.dim + 1) + 0.005 * np.sin(self.dim * 0.5)
        
        return adaptive_scale * (curvature_term + coupling_term + quantum_tunneling + penalty + basin_complexity)