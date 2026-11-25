import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales
        self.scales = np.logspace(0, 2, num=min(5, dim), base=10)
        self.amplitudes = np.logspace(1, -1, num=min(5, dim), base=10)
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base radial component with fractal scaling
        r = np.sqrt(np.sum(x_norm**2))
        
        # Multi-scale fractal modulation using different frequencies and amplitudes
        fractal_sum = 0.0
        for i, (scale, amp) in enumerate(zip(self.scales, self.amplitudes)):
            if i < len(x_norm):
                # Apply fractal-like oscillations at multiple scales
                freq = scale * (i + 1)
                fractal_sum += amp * np.sin(freq * r) * np.cos(freq * r**0.5)
        
        # Hierarchical multimodal structure with nested wells
        hierarchical_term = 0.0
        for i in range(min(3, self.dim)):
            # Create nested energy wells with varying depths
            well_depth = 1.0 / (i + 1)**1.5
            well_radius = 1.0 / (i + 1)**0.8
            # Distance to well center
            dist_to_center = np.sqrt(np.sum((x_norm - np.sin(i * np.pi/4) * np.ones(self.dim))**2))
            hierarchical_term += well_depth * np.exp(-dist_to_center**2 / (2 * well_radius**2))
        
        # Cross-dimensional coupling with fractal-like interactions
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            # Fractal-like interaction between adjacent dimensions
            coupling_strength = 0.3 * np.sin(3 * (x_norm[i] + x_norm[i+1]))
            cross_coupling += coupling_strength * np.cos(2 * (x_norm[i] - x_norm[i+1]))
        
        # Add a global periodic modulation to increase complexity
        global_mod = 0.5 * np.sin(2 * r) * np.cos(3 * r)
        
        # Combine all components with appropriate scaling
        total = 1.0 + fractal_sum + hierarchical_term + cross_coupling + global_mod
        
        # Ensure the function has a global minimum around the origin
        return np.abs(total) + 0.1 * r**2