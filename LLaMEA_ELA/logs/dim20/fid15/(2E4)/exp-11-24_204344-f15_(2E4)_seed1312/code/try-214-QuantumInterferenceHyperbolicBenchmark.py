import numpy as np

class QuantumInterferenceHyperbolicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Quantum interference pattern with sinusoidal modulation
        result = 0.0
        for i in range(self.dim):
            # Base quantum-like term with interference
            interference = np.sin(x[i] * (1.0 + 0.3 * np.cos(i * 0.5)))
            quantum_term = x[i]**2 + 0.5 * np.sinh(x[i]) * interference
            
            # Adaptive scaling based on position
            scale_factor = 1.0 + 0.2 * np.tanh(x[i])
            result += quantum_term * scale_factor
        
        # Hyperbolic coupling between dimensions
        hyperbolic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Hyperbolic sine coupling with dynamic phase
                phase = np.sin(x[i] * x[j] * (0.5 + 0.2 * np.sin(i * 0.3)))
                coupling = np.sinh(x[i]) * np.sinh(x[j]) * phase
                
                # Adaptive coupling strength
                strength = 0.7 + 0.3 * np.cos(i * 0.4 + j * 0.3)
                hyperbolic_coupling += strength * coupling
        
        # Gradient modulation with dynamic scaling
        gradient_mod = 0.0
        for i in range(self.dim):
            # Dynamic gradient based on position and dimension
            grad_factor = np.exp(-x[i]**2 * 0.1) * (1.0 + 0.5 * np.sin(i * 0.7))
            gradient_mod += grad_factor * x[i]**3
        
        # Adaptive penalty with exponential boundary influence
        penalty = 0.0
        for i in range(self.dim):
            # Boundary distance with exponential penalty
            dist_to_bound = min(5.0 - np.abs(x[i]), 0.1)
            if dist_to_bound < 0.5:
                penalty += 10.0 * np.exp(-dist_to_bound * 5.0) * x[i]**2
        
        # Multi-scale oscillatory component
        oscillation = 0.0
        for i in range(self.dim):
            # Multiple frequency oscillations with varying amplitudes
            freqs = [2.0, 4.0, 6.0, 8.0]
            osc_terms = []
            for f in freqs:
                term = np.sin(x[i] * f + i * 0.3) * np.cos(x[i] * f * 0.5)
                osc_terms.append(term)
            
            oscillation += np.mean(osc_terms) * (1.0 + 0.3 * np.cos(i * 0.6))
        
        # Combined landscape with weighted components
        total = 0.4 * result + 0.3 * hyperbolic_coupling + 0.2 * gradient_mod + 0.1 * penalty + 0.05 * oscillation
        
        # Global scaling factor that increases with dimensionality
        scaling = 1.0 + 0.15 * self.dim
        
        return total * scaling