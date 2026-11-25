import numpy as np

class ChaoticQuantumDefectBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for chaotic resonance wells
        self.resonance_frequencies = np.random.uniform(2.0, 15.0, dim)
        self.resonance_amplitudes = np.random.uniform(0.8, 4.0, dim)
        self.resonance_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Quantum-like superposition parameters
        self.superposition_weights = np.random.uniform(0.5, 1.5, dim)
        self.superposition_phases = np.random.uniform(0.0, 2*np.pi, dim)
        # Topological defect interaction parameters
        self.defect_strengths = np.random.uniform(1.5, 4.0, dim)
        self.defect_positions = np.random.uniform(-4.5, 4.5, dim)
        self.defect_radii = np.random.uniform(0.2, 1.5, dim)
        # Chaotic modulation parameters
        self.chaotic_parameters = np.random.uniform(0.5, 3.0, dim)
        self.chaotic_feedback = np.random.uniform(0.03, 0.7, (dim, dim))
        # Additional cubic and hyperbolic nonlinearities
        self.cubic_coefficients = np.random.uniform(0.1, 0.3, dim)
        self.hyperbolic_params = np.random.uniform(0.2, 0.8, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced chaotic resonance wells with quantum superposition and hyperbolic terms
        for i in range(self.dim):
            xi = x[i]
            freq = self.resonance_frequencies[i]
            amp = self.resonance_amplitudes[i]
            phase = self.resonance_phases[i]
            
            # Chaotic resonance term with feedback and hyperbolic modulation
            chaotic_term = amp * np.sin(freq * xi + phase)
            for j in range(self.dim):
                if i != j:
                    chaotic_term += self.chaotic_feedback[i][j] * np.sin(freq * x[j] + phase)
            
            # Hyperbolic and cubic nonlinearities
            hyperbolic_term = self.hyperbolic_params[i] * np.tanh(0.5 * freq * xi)
            cubic_term = self.cubic_coefficients[i] * xi**3
            
            # Quantum-like superposition with enhanced cubic nonlinearity
            superposition_term = self.superposition_weights[i] * np.cos(freq * xi + self.superposition_phases[i])
            quantum_effect = 0.5 * (chaotic_term**2 + superposition_term**2) + 0.2 * chaotic_term**3 + hyperbolic_term + cubic_term
            
            result += quantum_effect
            
        # Enhanced topological defect interactions with higher-order polynomial terms
        for i in range(self.dim):
            xi = x[i]
            defect_strength = self.defect_strengths[i]
            defect_pos = self.defect_positions[i]
            defect_radius = self.defect_radii[i]
            
            # Defect interaction with radial scaling, cubic and quartic terms
            distance = np.abs(xi - defect_pos)
            defect_interaction = defect_strength * np.exp(-0.5 * (distance / defect_radius)**2) + 0.1 * (distance / defect_radius)**3 + 0.05 * (distance / defect_radius)**4
            result += defect_interaction
            
        # Cross-dimensional chaotic coupling with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                chaos_strength = self.chaotic_parameters[i] * self.chaotic_parameters[j]
                
                # Chaotic cross-dimension coupling with cubic and quartic interaction
                chaotic_coupling = chaos_strength * np.sin(xi - xj) * np.cos(xi + xj) + 0.15 * (xi - xj)**3 + 0.08 * (xi - xj)**4
                result += chaotic_coupling
                
        # Adaptive quantum interference patterns with higher-order harmonics
        for i in range(self.dim):
            xi = x[i]
            interference = 0.5 * np.sin(2 * xi) * np.cos(3 * xi) + 0.1 * np.sin(5 * xi)**3 + 0.06 * np.sin(7 * xi)**4
            result += interference
            
        # Global chaotic modulation with enhanced spectral characteristics and multiple harmonics
        global_chaos = 1.0 + 1.5 * np.sin(np.sum(x) / self.dim)
        global_chaos *= (1.0 + 0.7 * np.cos(3.0 * np.sum(x)) + 0.2 * np.sin(2.0 * np.sum(x))**3 + 0.1 * np.cos(4.0 * np.sum(x))**2)
        result *= global_chaos
        
        # Add enhanced noise with higher-order polynomial terms
        noise = np.random.normal(0, 0.15, self.dim)
        for i in range(self.dim):
            result += noise[i] * np.sin(self.chaotic_parameters[i] * x[i]) + 0.08 * x[i]**3 + 0.03 * x[i]**4
            
        return result