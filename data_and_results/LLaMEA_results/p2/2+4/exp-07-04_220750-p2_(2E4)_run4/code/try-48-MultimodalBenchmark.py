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
        radial_term = r**6 + 0.4 * r**8 + 0.15 * r**10 + 0.05 * np.sin(10 * r * np.pi)
        
        # Implicit surface interaction terms with increased coupling strength
        surface_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Stronger coupled interaction with variable coupling coefficient
                coupling = 1.5 * np.sin(x_norm[i] * x_norm[j] * 3 * np.pi) * np.exp(-0.3 * r**2)
                surface_terms.append(coupling)
        
        # Multi-scale radial sinusoidal oscillation with variable frequency
        oscillation = np.sum(np.sin(9 * r * np.pi) + 0.6 * np.sin(18 * r * np.pi) + 0.2 * np.sin(27 * r * np.pi))
        
        # High-frequency multi-modal component with variable frequency and amplitude
        modal_component = np.sum(np.sin(30 * x_norm**2) + 0.4 * np.sin(60 * x_norm**2) + 0.1 * np.sin(90 * x_norm**2))
        
        # Cross-term interactions with enhanced complexity and nonlinearity
        cross_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear cross interaction with exponential decay
                cross = np.cos(x_norm[i] * x_norm[j] * 4 * np.pi) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
                cross_terms.append(cross)
        
        # Additional multi-modal structure with radial symmetry and phase shifts
        phase_shifts = np.linspace(0, 2*np.pi, self.dim, endpoint=False)
        radial_modulation = np.sum(np.sin(r * 5 * np.pi + phase_shifts) * np.exp(-0.2 * r**2))
        
        # Enhanced cross-dimensional coupling with trigonometric modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Additional coupling with trigonometric modulation
                mod = np.sin(x_norm[i] * x_norm[j] * 5 * np.pi) * np.cos(x_norm[i] + x_norm[j])
                cross_coupling += mod * np.exp(-0.1 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Additional quartic polynomial interaction terms for increased complexity
        quartic_terms = np.sum(x_norm**4) * 0.3
        
        # Combined fitness function with adjusted weights and enhanced complexity
        return radial_term + 0.2 * np.sum(surface_terms) + 0.1 * oscillation + 0.05 * modal_component + 0.07 * np.sum(cross_terms) + 0.03 * radial_modulation + 0.05 * cross_coupling + 0.1 * quartic_terms