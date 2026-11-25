import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion with stochastic resonance
        chaos_poly = 0
        for i in range(self.dim):
            # Basis functions with varying degrees and random coefficients
            basis1 = np.sin(2.0 * x[i]) + 0.5 * np.cos(3.0 * x[i])
            basis2 = x[i]**3 - 2.0 * x[i] + 1.0
            basis3 = np.exp(-0.5 * x[i]**2) * np.sin(4.0 * x[i])
            
            # Stochastic resonance effect with noise modulation
            noise_amp = 0.3 * (1.0 + 0.5 * np.sin(0.7 * x[i]))
            chaos_poly += basis1 * basis2 * basis3 * noise_amp
        
        # Adaptive neural network-like interactions
        nn_interaction = 0
        for i in range(self.dim):
            # Adaptive weights based on neighbor positions
            weight_sum = 0
            for j in range(max(0, i-3), min(i+4, self.dim)):
                if i != j:
                    distance = np.abs(x[i] - x[j])
                    # Dynamic weight based on position and dimension
                    weight = 1.0 + 0.8 * np.sin(0.5 * (x[i] + x[j]) + self.dim * 0.1)
                    weight_sum += weight * np.exp(-0.2 * distance**2)
            
            # Activation function with adaptive threshold
            activation = 1.0 / (1.0 + np.exp(-weight_sum))
            nn_interaction += activation * (x[i]**2 + 0.5 * np.sin(2.0 * x[i]))
        
        # Multi-scale oscillatory components with resonance peaks
        resonance = 0
        for i in range(self.dim):
            # Multiple frequencies with varying amplitudes
            freqs = [1.0, 2.0, 3.0, 4.0, 5.0]
            amps = [1.0, 0.8, 0.6, 0.4, 0.2]
            
            oscillation = 0
            for freq, amp in zip(freqs, amps):
                # Frequency modulation based on position
                mod_freq = freq * (1.0 + 0.3 * np.sin(0.2 * x[i]))
                oscillation += amp * np.sin(mod_freq * x[i]) * np.exp(-0.1 * x[i]**2)
            
            resonance += oscillation
        
        # Dynamic conditioning with time-varying parameters
        time_param = 1.5 + 0.5 * np.sin(0.3 * self.dim + 0.1 * np.sum(x))
        
        # Asymmetric multimodal structure with multiple local minima
        asymmetric = 0
        for i in range(self.dim):
            # Multiple quadratic wells with different centers and widths
            wells = [
                (x[i] - 2.0)**2 + 0.5 * np.sin(3.0 * x[i]),
                (x[i] + 2.0)**2 + 0.3 * np.cos(2.5 * x[i]),
                (x[i] - 1.0)**2 + 0.4 * np.sin(4.0 * x[i]),
                (x[i] + 1.0)**2 + 0.6 * np.cos(1.5 * x[i])
            ]
            
            # Stochastic selection of well
            selected_well = wells[np.abs(x[i]) % len(wells)]
            asymmetric += selected_well
        
        # Fractal-like ridge structures with self-similarity
        fractal_ridges = 0
        for i in range(self.dim):
            # Self-similar pattern at different scales
            scale1 = np.exp(-0.5 * (x[i] - 2.5)**2) * np.sin(3.0 * x[i])
            scale2 = np.exp(-0.3 * (x[i] + 2.5)**2) * np.cos(2.0 * x[i])
            scale3 = np.exp(-0.1 * x[i]**2) * np.sin(5.0 * x[i])
            
            fractal_ridges += scale1 + scale2 + scale3
        
        # Stochastic tunneling effects with quantum-like behavior
        tunneling = 0
        for i in range(self.dim):
            # Random tunneling probability
            tunnel_prob = 0.1 * (1.0 + np.sin(0.5 * x[i] + self.dim * 0.2))
            tunnel_effect = tunnel_prob * np.exp(-0.2 * (x[i] - 0.5)**2) * np.sin(6.0 * x[i])
            tunneling += tunnel_effect
        
        # Combine all components with optimized weights
        return time_param * (0.22 * chaos_poly + 0.23 * nn_interaction + 
                            0.21 * resonance + 0.15 * asymmetric + 0.12 * fractal_ridges + 0.10 * tunneling)