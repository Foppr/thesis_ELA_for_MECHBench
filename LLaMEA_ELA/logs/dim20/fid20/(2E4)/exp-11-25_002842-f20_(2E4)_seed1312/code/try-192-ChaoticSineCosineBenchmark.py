import numpy as np

class ChaoticSineCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for chaotic dynamics and time-delayed feedback
        self.freq_modulators = np.random.uniform(1.0, 3.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.amplitude_factors = np.random.uniform(0.5, 2.0, dim)
        self.delay_feedback_strengths = np.random.uniform(0.1, 0.8, dim)
        self.bifurcation_params = np.random.uniform(0.1, 1.5, dim)
        # Additional parameters for enhanced complexity and better fitness distribution
        self.nonlinear_exponents = np.random.uniform(1.2, 4.0, dim)
        self.damping_factors = np.random.uniform(0.02, 0.8, dim)
        self.resonance_centers = np.random.uniform(-3.0, 3.0, dim)
        self.harmonic_coefficients = np.random.uniform(0.1, 0.7, dim)
        self.adaptive_weights = np.random.uniform(0.4, 1.8, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base chaotic sine-cosine components with time-delayed feedback
        base_terms = 0.0
        for i in range(self.dim):
            freq = self.freq_modulators[i] * (1 + 0.3 * np.sin(x_norm[i]))
            # Add time-delayed feedback term
            delay_term = self.delay_feedback_strengths[i] * np.sin(x_norm[i] - 0.5 * x_norm[(i+1) % self.dim])
            base_terms += (self.amplitude_factors[i] * 
                          np.sin(freq * x_norm[i] + self.phase_shifts[i]) * 
                          np.cos(freq * x_norm[i] + self.phase_shifts[i]) * 
                          self.adaptive_weights[i] * 
                          (1 + 0.2 * delay_term))
        
        # Nonlinear transformation with adaptive exponents and saddle-node bifurcations
        nonlinear_terms = 0.0
        for i in range(self.dim):
            # Saddle-node bifurcation effect
            bifurcation_effect = 1 + self.bifurcation_params[i] * np.sin(x_norm[i])**2
            nonlinear_terms += (np.abs(x_norm[i])**self.nonlinear_exponents[i] * 
                              np.sin(x_norm[i]) * np.cos(x_norm[i]) * 
                              bifurcation_effect)
        
        # Cross-dimensional coupling with chaotic interactions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_interaction = (np.sin(x_norm[i] - x_norm[j]) * 
                                         np.cos(x_norm[i] + x_norm[j]) * 
                                         np.exp(-0.5 * (x_norm[i] - x_norm[j])**2))
                    coupling_terms += (0.5 * coupling_interaction * 
                                     (1 + 0.3 * np.sin(x_norm[i] * x_norm[j])) * 
                                     (1 + 0.2 * np.cos(x_norm[i] + x_norm[j])))
        
        # Resonance effects with chaotic centers and enhanced damping
        resonance_terms = 0.0
        for i in range(self.dim):
            # Chaotic resonance center effect
            chaos_center = self.resonance_centers[i] + 0.5 * np.sin(x_norm[i])
            resonance_terms += (np.exp(-0.5 * ((x_norm[i] - chaos_center)**2) / 
                                    (0.2 + 0.3 * np.abs(x_norm[i]))) * 
                              np.sin(2 * x_norm[i]) * 
                              (1 + 0.15 * np.cos(x_norm[i])))
        
        # Damping effects with chaotic parameters
        damping_terms = 0.0
        for i in range(self.dim):
            damping_terms += self.damping_factors[i] * np.exp(-x_norm[i]**2) * (1 + 0.15 * np.sin(x_norm[i]))
        
        # Additional harmonic components with chaotic coefficients
        harmonic_terms = 0.0
        for i in range(self.dim):
            # Add chaotic modulation to harmonic coefficients
            chaotic_coeff = self.harmonic_coefficients[i] * (1 + 0.2 * np.sin(x_norm[i]))
            harmonic_terms += chaotic_coeff * (np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[i]) + 
                                              0.6 * np.sin(5 * x_norm[i]))
        
        # Combine all terms with optimized weights for better fitness distribution
        return (0.3 * base_terms + 
                0.25 * nonlinear_terms + 
                0.2 * coupling_terms + 
                0.15 * resonance_terms + 
                0.08 * damping_terms + 
                0.02 * harmonic_terms)