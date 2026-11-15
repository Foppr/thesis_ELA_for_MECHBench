import numpy as np

class ChaoticAsymmetricSaddle:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Base chaotic component with nested sinusoids and increased complexity
        f = 0.0
        for i in range(self.dim):
            f += np.sin(3 * x_norm[i]) * np.cos(5 * x_norm[i]) * np.sin(7 * x_norm[i]) * np.cos(9 * x_norm[i])
            
        # Asymmetric saddle points with enhanced dynamic weights and non-linear bias
        for i in range(self.dim):
            # Asymmetric quadratic terms with directional bias and chaotic modulation
            bias = 0.5 * np.sin(i * 0.7) + 0.2 * np.cos(i * 1.3)
            f += (x[i]**2 + bias * x[i]) * np.tanh(x[i]) + 0.3 * np.sinh(x[i]**2) + 0.1 * np.sin(11 * x[i])
            
        # Nested multi-scale modulations with increased coupling and fractal-like structure
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling
                modulation = np.sin(2 * x_norm[i]) * np.cos(3 * x_norm[j]) * np.sin(5 * x_norm[i]) * np.cos(7 * x_norm[j])
                f += 0.3 * modulation * (1 + 0.1 * np.sin(i + j) + 0.05 * np.cos(i * j))
                
        # Dynamic gradient landscape based on proximity to critical points with enhanced sensitivity
        proximity = 0.0
        for i in range(self.dim):
            proximity += np.abs(x[i] - np.sin(i * 0.5)) + 0.1 * np.abs(x[i] - np.cos(i * 0.3))
        scale_factor = 1.0 + 0.8 * np.exp(-proximity / 1.5)
        f *= scale_factor
        
        # Fractal-like complexity with recursive harmonic terms and increased dimensionality
        for i in range(self.dim):
            f += 0.15 * np.sin(13 * x_norm[i]) * np.cos(17 * x_norm[i]) * np.sin(19 * x_norm[i]) * np.cos(23 * x_norm[i])
            
        # Chaotic perturbations with higher frequency components and increased amplitude
        chaos = 0.0
        for i in range(self.dim):
            chaos += np.sin(23 * x_norm[i]) * np.cos(29 * x_norm[i]) * np.sin(31 * x_norm[i]) * np.cos(37 * x_norm[i])
        f += 0.1 * chaos
        
        # Strengthened global minimum attraction with higher-order polynomial terms
        f += 0.3 * np.sum(x**6) + 0.1 * np.sum(x**8)
        
        # Additional multi-modal structure with periodic peaks
        for i in range(self.dim):
            f += 0.2 * np.sin(10 * x[i]) * np.cos(15 * x[i]) * np.sin(20 * x[i])
            
        # Enhanced noise and irregularity with additional chaotic harmonic components
        noise = 0.0
        for i in range(self.dim):
            noise += 0.05 * np.sin(41 * x_norm[i]) * np.cos(43 * x_norm[i]) + 0.03 * np.sin(47 * x_norm[i]) * np.cos(53 * x_norm[i])
        f += noise
        
        # Introduce irregular coupling between dimensions with dynamic weights
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                dynamic_weight = 0.2 * np.sin(i * 0.3) * np.cos(j * 0.4) + 0.1 * np.sin(i * j * 0.1)
                f += dynamic_weight * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Add irregular fractal-like structures with recursive harmonic terms
        for i in range(self.dim):
            f += 0.05 * np.sin(29 * x_norm[i]) * np.cos(37 * x_norm[i]) * np.sin(41 * x_norm[i]) * np.cos(47 * x_norm[i]) * np.sin(53 * x_norm[i])
            
        # Introduce chaotic modulation with exponential decay and increased sensitivity
        exp_mod = 0.0
        for i in range(self.dim):
            exp_mod += np.exp(-0.5 * x[i]**2) * np.sin(61 * x_norm[i]) * np.cos(67 * x_norm[i])
        f += 0.15 * exp_mod
        
        # Add multi-scale periodicity with non-uniform frequencies and amplitudes
        periodicity = 0.0
        for i in range(self.dim):
            periodicity += 0.1 * np.sin(25 * x[i]) * np.cos(30 * x[i]) * np.sin(35 * x[i]) * np.cos(40 * x[i])
        f += periodicity
        
        # Enhanced chaotic sensitivity with higher-order coupling terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                for k in range(j+1, min(j+4, self.dim)):
                    coupling += 0.05 * np.sin(x[i] + x[j] + x[k]) * np.cos(x[i] - x[j] + x[k])
        f += coupling
        
        # Additional chaotic modulation with higher frequency components and increased amplitude
        chaos2 = 0.0
        for i in range(self.dim):
            chaos2 += np.sin(53 * x_norm[i]) * np.cos(59 * x_norm[i]) * np.sin(61 * x_norm[i]) * np.cos(67 * x_norm[i]) * np.sin(71 * x_norm[i])
        f += 0.12 * chaos2
        
        # Multi-scale harmonic coupling with exponentially decaying weights
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):
                weight = 0.15 * np.exp(-0.1 * (i + j))
                f += weight * np.sin(3 * x[i]) * np.cos(4 * x[j]) * np.sin(5 * x[i]) * np.cos(6 * x[j])
                
        # Enhanced saddle point structure with irregular perturbations
        for i in range(self.dim):
            f += 0.25 * np.sin(2 * x[i]) * np.cos(3 * x[i]) * np.sin(4 * x[i]) * np.cos(5 * x[i]) * np.sin(6 * x[i])
            
        # Increased fractal dimensionality with recursive nested terms
        for i in range(self.dim):
            f += 0.08 * np.sin(73 * x_norm[i]) * np.cos(79 * x_norm[i]) * np.sin(83 * x_norm[i]) * np.cos(89 * x_norm[i]) * np.sin(97 * x_norm[i]) * np.cos(101 * x_norm[i])
            
        # Enhanced multi-modal structure with irregular peaks
        for i in range(self.dim):
            f += 0.18 * np.sin(12 * x[i]) * np.cos(18 * x[i]) * np.sin(24 * x[i]) * np.cos(30 * x[i])
            
        # Additional chaotic interference with increased complexity
        interference = 0.0
        for i in range(self.dim):
            interference += 0.07 * np.sin(103 * x_norm[i]) * np.cos(107 * x_norm[i]) * np.sin(109 * x_norm[i])
        f += interference
        
        # Adaptive gradient modulation with dynamic scaling factors
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += 0.2 * np.sin(113 * x[i]) * np.cos(127 * x[i]) * np.sin(131 * x[i]) * np.cos(137 * x[i])
        f += 0.1 * grad_mod
        
        # Final scaling to ensure global minimum is well-defined
        f *= 1.0 + 0.05 * np.sum(np.abs(x))
        
        # Introduce a new highly complex chaotic component with 100+ harmonic terms
        complex_chaos = 0.0
        for i in range(self.dim):
            for k in range(1, 21):  # 20 harmonic components
                complex_chaos += 0.01 * np.sin(k * 13 * x_norm[i]) * np.cos(k * 17 * x_norm[i]) * np.sin(k * 19 * x_norm[i]) * np.cos(k * 23 * x_norm[i])
        f += complex_chaos
        
        # Add a new multi-modal structure with irregularly spaced peaks
        irregular_peaks = 0.0
        for i in range(self.dim):
            irregular_peaks += 0.15 * np.sin(31 * x[i]) * np.cos(41 * x[i]) * np.sin(53 * x[i]) * np.cos(67 * x[i]) * np.sin(73 * x[i])
        f += irregular_peaks
        
        # Introduce a new fractal-like structure with exponentially increasing frequency components
        fractal_structure = 0.0
        for i in range(self.dim):
            for k in range(1, 11):
                fractal_structure += 0.02 * np.sin(k**2 * 29 * x_norm[i]) * np.cos(k**2 * 37 * x_norm[i]) * np.sin(k**2 * 41 * x_norm[i])
        f += fractal_structure
        
        # Add a new chaotic interference pattern with irregular phase shifts
        phase_shifted_interference = 0.0
        for i in range(self.dim):
            phase_shifted_interference += 0.08 * np.sin(89 * x_norm[i] + 0.3 * i) * np.cos(97 * x_norm[i] + 0.4 * i) * np.sin(101 * x_norm[i] + 0.5 * i)
        f += phase_shifted_interference
        
        # Introduce a new multi-scale harmonic coupling with dynamic coupling strengths
        dynamic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                dynamic_weight = 0.1 * np.sin(i * 0.2) * np.cos(j * 0.3) * np.sin(i * j * 0.05) * np.cos(i + j * 0.1)
                dynamic_coupling += dynamic_weight * np.sin(2 * x[i] + 3 * x[j]) * np.cos(3 * x[i] - 2 * x[j])
        f += dynamic_coupling
        
        # Add a new chaotic modulation with multi-exponential decay
        multi_exp_mod = 0.0
        for i in range(self.dim):
            multi_exp_mod += np.exp(-0.3 * x[i]**2) * np.exp(-0.2 * x[i]**4) * np.sin(103 * x_norm[i]) * np.cos(107 * x_norm[i])
        f += 0.2 * multi_exp_mod
        
        # Final adjustment to ensure proper scaling and global minimum positioning
        f += 0.05 * np.sum(x**10)
        
        # Slight mutation: adjusted coupling weights and harmonic frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                f += 0.08 * np.sin(4 * x[i]) * np.cos(6 * x[j]) * np.sin(8 * x[i]) * np.cos(10 * x[j])  # Modified coupling
        for i in range(self.dim):
            f += 0.22 * np.sin(14 * x[i]) * np.cos(19 * x[i]) * np.sin(23 * x[i]) * np.cos(29 * x[i])  # Changed frequencies
        
        return f