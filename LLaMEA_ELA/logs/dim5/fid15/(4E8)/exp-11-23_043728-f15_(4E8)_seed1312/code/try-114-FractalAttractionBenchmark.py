import numpy as np

class FractalAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 3.1  # Increased fractional dimension for more complex structure
        self.attraction_strength = 2.5
        self.frequency_base = 6.0
        self.quantum_factor = 1.2
        self.adaptive_coupling = 0.4
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create quantum-inspired fractal pattern with interference effects
        fractal_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            scale = 2 ** (i % 7)
            freq = self.frequency_base * scale
            # Quantum interference terms with higher-order complexity
            quantum_term = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.3) * \
                          np.sin(freq * x_norm[i] * 0.7) * np.cos(freq * x_norm[i] * 1.2) * \
                          np.sin(freq * x_norm[i] * 2.1) * np.cos(freq * x_norm[i] * 3.4)
            fractal_pattern[i] = quantum_term + 0.4 * np.sin(freq * x_norm[i] * 2.0) + \
                                0.2 * np.sin(freq * x_norm[i] * 4.0)
        
        # Enhanced attraction fields with dynamic basins and chaotic coupling
        attraction_fields = np.zeros(self.dim)
        for i in range(self.dim):
            center_points = np.array([-0.9, -0.7, -0.4, -0.1, 0.2, 0.5, 0.8])
            strengths = np.array([1.8, 1.5, 1.1, 0.9, 1.2, 0.8, 1.6])
            
            distances = np.abs(x_norm[i] - center_points)
            attraction_fields[i] = np.sum(strengths * np.exp(-distances**3.0))
        
        # Combine fractal pattern with enhanced attraction fields
        combined_pattern = fractal_pattern + 0.7 * attraction_fields
        
        # Add quantum-inspired curvature terms with higher-order polynomials and chaotic scaling
        curvature_term = np.sum(combined_pattern**6) + 0.5 * np.sum(combined_pattern**8)
        
        # Introduce dynamic coupling with time-like progression and chaotic modulation
        coupling_term = self.adaptive_coupling * np.sum((x_norm[1:] - x_norm[:-1])**5) * \
                       (1.0 + 0.2 * np.sin(self.dim * 0.3))
        
        # Add quantum tunneling effects and non-smooth features with chaotic modulation
        quantum_tunneling = 0.4 * np.sum(np.abs(x_norm)**1.5) * (1.0 + 0.1 * np.cos(self.dim * 0.7))
        
        # Introduce adaptive penalty based on dimensionality and solution distribution with chaotic scaling
        penalty = 0.15 * self.dim * (np.std(x_norm)**2 + 0.08 * np.mean(np.abs(x_norm))) * \
                 (1.0 + 0.15 * np.sin(self.dim * 0.4))
        
        # Add basin complexity factor that scales with dimensionality and chaotic modulation
        basin_complexity = 0.1 * self.dim * np.sum(np.sin(4.0 * x_norm)**2) * \
                          (1.0 + 0.1 * np.cos(self.dim * 0.6))
        
        # Final fitness calculation with enhanced adaptive scaling and chaotic modulation
        adaptive_scale = 1.0 + 0.03 * np.log(self.dim + 1) + 0.01 * np.sin(self.dim * 0.7) + \
                        0.008 * np.cos(self.dim * 0.5)
        
        return adaptive_scale * (curvature_term + coupling_term + quantum_tunneling + penalty + basin_complexity)