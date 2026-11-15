import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Radial component with higher-order polynomial growth and nonlinearity
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = r**7 + 0.5 * r**9 + 0.2 * r**11 + 0.08 * np.sin(12 * r * np.pi)
        
        # Implicit surface interaction terms with increased coupling strength
        surface_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger coupled interaction with variable coupling coefficient
                coupling = 2.0 * np.sin(x_norm[i] * x_norm[j] * 4 * np.pi) * np.exp(-0.4 * r**2)
                surface_terms.append(coupling)
        
        # Multi-scale radial sinusoidal oscillation with variable frequency
        oscillation = np.sum(np.sin(11 * r * np.pi) + 0.7 * np.sin(22 * r * np.pi) + 0.3 * np.sin(33 * r * np.pi))
        
        # High-frequency multi-modal component with variable frequency and amplitude
        modal_component = np.sum(np.sin(35 * x_norm**2) + 0.5 * np.sin(70 * x_norm**2) + 0.15 * np.sin(105 * x_norm**2))
        
        # Cross-term interactions with enhanced complexity and nonlinearity
        cross_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear cross interaction with exponential decay
                cross = np.cos(x_norm[i] * x_norm[j] * 5 * np.pi) * np.exp(-0.6 * (x_norm[i]**2 + x_norm[j]**2))
                cross_terms.append(cross)
        
        # Additional multi-modal structure with radial symmetry and phase shifts
        phase_shifts = np.linspace(0, 2*np.pi, self.dim, endpoint=False)
        radial_modulation = np.sum(np.sin(r * 6 * np.pi + phase_shifts) * np.exp(-0.3 * r**2))
        
        # Combined fitness function with adjusted weights and enhanced complexity
        return radial_term + 0.3 * np.sum(surface_terms) + 0.15 * oscillation + 0.1 * modal_component + 0.1 * np.sum(cross_terms) + 0.05 * radial_modulation