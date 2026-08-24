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
                # Slightly stronger coupled interaction with modified coupling coefficient
                coupling = 1.7 * np.sin(x_norm[i] * x_norm[j] * 3.5 * np.pi) * np.exp(-0.35 * r**2)
                surface_terms.append(coupling)
        
        # Multi-scale radial sinusoidal oscillation with variable frequency
        oscillation = np.sum(np.sin(9.5 * r * np.pi) + 0.6 * np.sin(18.5 * r * np.pi) + 0.2 * np.sin(27.5 * r * np.pi))
        
        # High-frequency multi-modal component with variable frequency and amplitude
        modal_component = np.sum(np.sin(32 * x_norm**2) + 0.4 * np.sin(62 * x_norm**2) + 0.1 * np.sin(92 * x_norm**2))
        
        # Cross-term interactions with enhanced complexity and nonlinearity
        cross_terms = []
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Nonlinear cross interaction with exponential decay
                cross = np.cos(x_norm[i] * x_norm[j] * 4.2 * np.pi) * np.exp(-0.55 * (x_norm[i]**2 + x_norm[j]**2))
                cross_terms.append(cross)
        
        # Additional multi-modal structure with radial symmetry and phase shifts
        phase_shifts = np.linspace(0, 2*np.pi, self.dim, endpoint=False)
        radial_modulation = np.sum(np.sin(r * 5.5 * np.pi + phase_shifts) * np.exp(-0.22 * r**2))
        
        # Combined fitness function with adjusted weights and enhanced complexity
        return radial_term + 0.22 * np.sum(surface_terms) + 0.11 * oscillation + 0.06 * modal_component + 0.08 * np.sum(cross_terms) + 0.035 * radial_modulation