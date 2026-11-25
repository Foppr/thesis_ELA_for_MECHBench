import numpy as np

class FractalAttractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.fractal_dim = 2.8  # Increased fractional dimension for more complex structure
        self.attraction_strength = 1.8
        self.frequency_base = 5.0
        self.quantum_factor = 0.9
        self.adaptive_coupling = 0.3
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = np.clip(x / 5.0, -1, 1)
        
        # Create enhanced quantum-inspired fractal pattern with interference effects
        fractal_pattern = np.zeros(self.dim)
        for i in range(self.dim):
            scale = 2 ** (i % 6)
            freq = self.frequency_base * scale
            # Enhanced quantum interference terms
            quantum_term = np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i] * 0.4) * \
                          np.sin(freq * x_norm[i] * 0.8) * np.cos(freq * x_norm[i] * 1.5) * \
                          np.sin(freq * x_norm[i] * 0.2)
            fractal_pattern[i] = quantum_term + 0.4 * np.sin(freq * x_norm[i] * 2.5)
        
        # Enhanced attraction fields with dynamic basins and multi-scale centers
        attraction_fields = np.zeros(self.dim)
        for i in range(self.dim):
            center_points = np.array([-0.8, -0.6, -0.3, 0.1, 0.4, 0.7, 0.9])
            strengths = np.array([1.6, 1.3, 0.9, 1.1, 0.8, 1.4, 1.2])
            
            distances = np.abs(x_norm[i] - center_points)
            attraction_fields[i] = np.sum(strengths * np.exp(-distances**3.0))
        
        # Combine fractal pattern with enhanced attraction fields
        combined_pattern = fractal_pattern + 0.7 * attraction_fields
        
        # Add enhanced quantum curvature terms with higher-order polynomials
        curvature_term = np.sum(combined_pattern**6) + 0.5 * np.sum(combined_pattern**8)
        
        # Introduce stronger dynamic coupling with time-like progression
        coupling_term = self.adaptive_coupling * np.sum((x_norm[1:] - x_norm[:-1])**5)
        
        # Add enhanced quantum tunneling effects and non-smooth features
        quantum_tunneling = 0.4 * np.sum(np.abs(x_norm)**1.4)
        
        # Introduce adaptive penalty based on dimensionality and solution distribution
        penalty = 0.15 * self.dim * (np.std(x_norm)**2 + 0.08 * np.mean(np.abs(x_norm)))
        
        # Add enhanced basin complexity factor that scales with dimensionality
        basin_complexity = 0.1 * self.dim * np.sum(np.sin(4.0 * x_norm)**2)
        
        # Final fitness calculation with enhanced adaptive scaling
        adaptive_scale = 1.0 + 0.03 * np.log(self.dim + 1) + 0.008 * np.sin(self.dim * 0.6)
        
        return adaptive_scale * (curvature_term + coupling_term + quantum_tunneling + penalty + basin_complexity)