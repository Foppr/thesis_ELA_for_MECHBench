import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2) * 0.1
        
        # Enhanced chaotic gradient component with multiple attractors and memory effects
        chaotic_grad = 0
        for i in range(self.dim):
            # Multiple chaotic mappings with different frequencies, amplitudes, and phase shifts
            freq1 = 2.8 + 0.4 * np.sin(i * 0.7)
            freq2 = 3.2 + 0.2 * np.cos(i * 0.9)
            freq3 = 2.0 + 0.3 * np.sin(0.5 * i * 1.2)
            
            # Chaotic terms with varying scales and memory effects
            term1 = np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) * np.exp(-0.5 * x[i]**2)
            term2 = np.cos(freq3 * x[i]) * np.sin(freq1 * x[i]) * np.exp(-0.3 * (x[i] - 1.8)**2)
            term3 = np.sin(freq2 * x[i]) * np.cos(freq3 * x[i]) * np.exp(-0.4 * (x[i] + 1.5)**2)
            
            # Memory effect: incorporate previous dimension's contribution
            memory_factor = 0.12 * np.sin(0.2 * i) if i > 0 else 0
            chaotic_grad += (term1 + term2 + term3) * (1.0 + 0.25 * np.sin(0.3 * i) + memory_factor)
        
        # Saddle point component with variable conditioning and dynamic locations
        saddle = 0
        for i in range(self.dim):
            # Create dynamic saddle points at different locations based on dimension index
            saddle_loc = 2.2 * np.sin(i * 0.5) * (1.0 + 0.12 * np.cos(i * 0.3))
            condition_factor = 1.0 + 0.45 * np.cos(i * 0.3) * np.sin(0.2 * i)
            
            # Saddle point function with varying curvature and dynamic scaling
            saddle_term = (x[i] - saddle_loc)**2 * (x[i] - saddle_loc)**4 * condition_factor
            saddle += saddle_term
        
        # Multi-scale oscillatory component with enhanced nonlinearity
        oscillatory = 0
        scales = [0.6, 1.2, 2.2, 3.8, 4.5]
        for i in range(self.dim):
            scale_idx = i % len(scales)
            scale = scales[scale_idx]
            
            # Multi-frequency oscillation with variable amplitude and enhanced chaos
            osc_term = np.sin(scale * x[i]) * np.cos(1.5 * scale * x[i]) * np.exp(-0.1 * (x[i] - 2.2)**2)
            osc_term += np.cos(scale * x[i]) * np.sin(2.0 * scale * x[i]) * np.exp(-0.15 * (x[i] + 2.2)**2)
            
            # Add chaotic modulation to oscillatory component
            chaos_mod = 0.12 * np.sin(0.5 * scale * x[i])
            osc_term += chaos_mod
            
            oscillatory += osc_term * (1.0 + 0.12 * np.sin(i * 0.4))
        
        # Cross-dimensional interaction with dynamic weights and enhanced coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased interaction range
                weight = 0.7 + 0.15 * np.sin(0.2 * (i + j)) * np.cos(0.1 * i)
                interaction += weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Variable dimension coupling with dynamic scaling and chaotic modulation
        coupling = 0
        for i in range(self.dim):
            coupling_factor = 1.0 + 0.35 * np.sin(0.4 * i) * np.cos(0.3 * i)
            coupling += (np.sin(x[i] * coupling_factor) * np.cos(x[i] * coupling_factor) * 
                        np.exp(-0.2 * x[i]**2) * coupling_factor)
        
        # Asymmetric chaotic modulation with enhanced complexity
        asymmetric = 0
        for i in range(self.dim):
            asym_factor = 1.0 + 0.38 * np.sin(0.3 * i) * np.cos(0.2 * i)
            asym_term = (np.sin(x[i] * asym_factor) * np.exp(-0.1 * x[i]**2) + 
                        np.cos(x[i] * asym_factor) * np.exp(-0.15 * x[i]**2))
            asymmetric += asym_term
        
        # Hybrid polynomial-chaotic with memory and enhanced multimodal structure
        memory = 0
        for i in range(self.dim):
            # Enhanced memory effect with chaotic coupling
            mem_factor = 0.22 * np.sin(0.1 * i)
            memory += (np.sin(x[i]**3) * np.cos(x[i]) * np.exp(-0.1 * (x[i] - 1.2)**2) + 
                      np.cos(x[i]**2) * np.sin(x[i]) * np.exp(-0.15 * (x[i] + 1.2)**2) + mem_factor)
        
        # Enhanced multimodal structure with dynamic peaks and chaotic modulation
        multimodal = 0
        for i in range(self.dim):
            # Dynamic peak locations and heights based on dimension index with chaotic variation
            peak_loc = 1.7 * np.sin(0.3 * i) * (1.0 + 0.12 * np.cos(i * 0.2))
            peak_height = 1.1 + 0.35 * np.cos(0.2 * i) * np.sin(0.1 * i)
            
            # Multi-peak chaotic function with varying distances and enhanced nonlinearity
            multimodal += peak_height * (np.sin(x[i] - peak_loc) * np.exp(-0.2 * (x[i] - peak_loc)**2) +
                                       np.cos(x[i] + peak_loc) * np.exp(-0.15 * (x[i] + peak_loc)**2))
        
        # Add new component: fractal-like chaotic structure with self-similarity
        fractal = 0
        for i in range(self.dim):
            # Fractal modulation using recursive-like behavior
            fractal_term = np.sin(x[i]**2) * np.cos(x[i]) * np.exp(-0.1 * x[i]**2)
            fractal_term += np.cos(x[i]**3) * np.sin(x[i]) * np.exp(-0.05 * (x[i] - 1.2)**2)
            fractal += fractal_term * (1.0 + 0.22 * np.sin(0.4 * i))
        
        # Add new component: multi-scale chaotic interference patterns
        interference = 0
        for i in range(self.dim):
            # Interference between multiple chaotic frequencies
            freq_a = 1.2 + 0.4 * np.sin(i * 0.3)
            freq_b = 2.2 + 0.25 * np.cos(i * 0.4)
            interference += (np.sin(freq_a * x[i]) * np.cos(freq_b * x[i]) * 
                           np.exp(-0.1 * (x[i] - 0.6)**2) +
                           np.cos(freq_a * x[i]) * np.sin(freq_b * x[i]) * 
                           np.exp(-0.15 * (x[i] + 0.6)**2))
        
        # Add new component: enhanced gradient coupling with dynamic scaling
        gradient_coupling = 0
        for i in range(self.dim):
            # Dynamic coupling based on neighbor dimensions
            if i > 0:
                grad_coupling = np.sin(x[i-1] * x[i]) * np.cos(x[i-1] + x[i]) * np.exp(-0.1 * (x[i-1]**2 + x[i]**2))
                gradient_coupling += grad_coupling * (1.0 + 0.15 * np.sin(0.3 * i))
        
        # Add new component: enhanced local minima clustering with chaotic modulation
        local_minima = 0
        for i in range(self.dim):
            # Clustered local minima locations
            cluster_loc = 2.7 * np.sin(0.4 * i) * (1.0 + 0.12 * np.cos(i * 0.2))
            cluster_height = 0.9 + 0.25 * np.cos(0.3 * i)
            local_minima += cluster_height * (np.exp(-0.5 * (x[i] - cluster_loc)**2) + 
                                             np.exp(-0.3 * (x[i] + cluster_loc)**2))
        
        # Combine all components with optimized weights
        return (quadratic * 0.7 +
                chaotic_grad * 0.45 +
                saddle * 0.35 +
                oscillatory * 0.55 +
                interaction * 0.3 +
                coupling * 0.18 +
                asymmetric * 0.25 +
                memory * 0.18 +
                multimodal * 0.3 +
                fractal * 0.15 +
                interference * 0.2 +
                gradient_coupling * 0.12 +
                local_minima * 0.18)